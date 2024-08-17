from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CreateApprovalAPIView, PackageViewSet, TruckViewSet, VisualizePackagesView

router = DefaultRouter()
router.register(r"packages", PackageViewSet)
router.register(r"trucks-boarding", TruckViewSet, basename="truck")

urlpatterns = [
    path("", include(router.urls)),
    path("visualize-packages/", VisualizePackagesView.as_view(), name="visualize_packages"),
    path("approval/", CreateApprovalAPIView.as_view(), name="approval"),
]
