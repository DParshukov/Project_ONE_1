import pytest
from rest_framework.test import APIClient
from hotel.models import Room, Booking

@pytest.mark.django_db
def test_create_booking_nonexistent_room():
    client=APIClient()
    url='/booking/create/'
    data={
        'room_id':5,
        'date_start':'2025-09-4',
        'date_end':'2025-09-16'
    }
    response=client.post(url, data, format='json')
    assert response.status_code == 400

@pytest.mark.django_db
def test_create_room_without_description():
    client=APIClient()
    url='/room/create/'
    data={
        'price':5000
    }
    response=client.post(url, data, format='json')
    assert response.status_code == 400

@pytest.mark.django_db
def test_delete_nonexistent_room():
    client = APIClient()
    url = '/room/delete/99999/'
    response = client.delete(url)
    assert response.status_code == 404