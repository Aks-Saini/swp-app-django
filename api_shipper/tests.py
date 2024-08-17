from decimal import Decimal

import pytest

from .models import Package, Truck


@pytest.mark.django_db
def test_truck_creation():
    truck_data = {
        "model_name": "Volvo FH16",
        "length": Decimal("6.00"),
        "breadth": Decimal("2.50"),
        "height": Decimal("3.50"),
        "tare_weight": Decimal("7000.00"),
        "gvwr": Decimal("18000.00"),
        "axle_weight_ratings": [4000.0, 4500.0],
        "axle_group_weight_ratings": [8000.0],
        "wheel_load_capacity": Decimal("12000.00"),
        "destination": "San Francisco",
        "status": "entered",
    }
    truck = Truck.objects.create(**truck_data)
    assert truck.model_name == "Volvo FH16"
    assert truck.destination == "SAN FRANCISCO"  # checking save method effect


@pytest.mark.django_db
def test_truck_str():
    truck = Truck(model_name="Volvo FH16", gvwr=Decimal("18000.00"))
    assert str(truck) == f"Truck {truck.id} - GVWR: 18000.00 kg"


@pytest.mark.django_db
def test_package_creation():
    package_data = {
        "name": "Electronics",
        "length": Decimal("1.00"),
        "breadth": Decimal("0.50"),
        "height": Decimal("0.25"),
        "weight": Decimal("20.00"),
        "destination": "New York",
        "deliver_date": "2023-01-01",
        "stock": 10,
    }
    package = Package.objects.create(**package_data)
    assert package.name == "Electronics"
    assert package.destination == "NEW YORK"  # checking save method effect


@pytest.mark.django_db
def test_package_volume():
    package = Package(length=Decimal("1.00"), breadth=Decimal("0.50"), height=Decimal("0.25"))
    assert package.volume == Decimal("0.125")  # L * B * H
