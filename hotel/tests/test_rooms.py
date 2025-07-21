from http.client import responses

from django.test import TestCase
import pytest
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_create_room():
    client=APIClient()
    url='/room/create/'
    data={
        'description':'Комната у дороги',
        'price':5000
    }
    response=client.post(url, data, format='json')
    assert response.status_code == 201 or response.status_code == 200
    assert 'room' in response.data


@pytest.mark.django_db
def test_get_list_room():
    client=APIClient()
    url='/rooms/list/'
    from hotel.models import Room
    room1 = Room.objects.create(description='room 1', price=6000)
    room2 = Room.objects.create(description='room 2', price=4500)
    room3 = Room.objects.create(description='room 3', price=3000)

    response=client.get(url)
    assert response.status_code == 200
    assert isinstance(response.data, list)
    assert len(response.data) == 3
    prices=[float(room['price']) for room in response.data]
    assert room1.price in prices
    assert room2.price in prices
    assert room3.price in prices

@pytest.mark.django_db
def test_delete_room():
    client=APIClient()
    url='/room/delete/1/'
    from hotel.models import Room
    room1=Room.objects.create(description='room 1', price=6000)
    response=client.delete(url)
    assert response.status_code == 200
    assert 'detail' in response.data


# Create your tests here.
