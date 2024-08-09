# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Package, Truck
from .serializers import PackageSerializer, TruckSerializer
from rest_framework.views import APIView
import requests
import http.client
import json
from django.http import JsonResponse
from api_shipper.tasks import call_visualizer_microservice
import random

class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class TruckViewSet(viewsets.ModelViewSet):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)





class VisualizePackagesView(APIView):
    def post(self, request, *args, **kwargs):
        truck_id = request.data.get('truck_id')

        if not truck_id:
            return Response({'error': 'Truck ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Retrieve the truck based on the provided ID
            truck = Truck.objects.get(id=truck_id)
            
            # Retrieve packages with the same destination and status 'inventory'
            packages = Package.objects.filter(
                destination=truck.destination,
                status='inventory'
            )
            
            truck_data = {
                'id': str(truck.id),
                'model_name': truck.model_name,
                'length': int(truck.length),  # Convert to integer
                'breadth': int(truck.breadth),  # Convert to integer
                'height': int(truck.height),  # Convert to integer
                'tare_weight': int(truck.tare_weight),  # Convert to integer
                'gvwr': int(truck.gvwr),  # Convert to integer
                'axle_weight_ratings': [int(x) for x in truck.axle_weight_ratings],  # Convert list items to integers
                'axle_group_weight_ratings': [int(x) for x in truck.axle_group_weight_ratings],  # Convert list items to integers
                'wheel_load_capacity': int(truck.wheel_load_capacity),  # Convert to integer
            }

            packages_data = [
                {
                    'id': str(pkg.id),
                    'length': int(pkg.length),  # Convert to integer
                    'breadth': int(pkg.breadth),  # Convert to integer
                    'height': int(pkg.height),  # Convert to integer
                    'weight': int(pkg.weight),
                    'box_id': pkg.name,
                    'stock' : pkg.stock,
                    # 'priority': pkg.priority,   # Convert to integer
                    # 'priority': 3,

                }
                for pkg in packages
            ]
            # random.shuffle(packages_data)
            # Prepare data to send to external server
            data_to_send = {
                'truck': truck_data,
                'boxes': packages_data
            }
            # call_visualizer_microservice.delay(data_to_send)
            external_server_url = 'http://swp_visualizer:8081/process/'
            headers = {'Content-Type': 'application/json'}
            try:
                response = requests.post(url=external_server_url, headers=headers, json=data_to_send)
                response.raise_for_status()
                allocated_boxes = response.json().get("box_ids", None)

                if allocated_boxes:
                    for box_id in allocated_boxes:
                        print("*********************", box_id)
                        try:
                            package = Package.objects.get(name=box_id, destination=truck.destination)
                            package.status = "allocated"
                            package.allocation = truck.model_name
                            package.save()
                        except Package.DoesNotExist:
                            print(f"Package with name {box_id} and destination {truck.destination} does not exist.")
                else:
                    print("No box_ids found in the response.")

                return JsonResponse({'message': 'Visualization Task Submitted'}, status=status.HTTP_202_ACCEPTED)
            except requests.RequestException as e:
                return {'error': str(e)}
        
        except Exception as e:
            return JsonResponse({'error': f'An error occurred: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)