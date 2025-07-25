import pytest
from rest_framework.test import APIClient
from hotel.models import Room, Booking
@pytest.mark.django_db
def test_create_booking():
    client=APIClient()
    url='/booking/create/'
    data={
        'room_id':1,
        'date_start':'2025-12-1',
        'date_end':'2025-12-6'
    }
    room1 = Room.objects.create(description='room 1', price=6000)
    response=client.post(url, data, format='json')
    assert response.status_code == 201
    a=response.data
    assert response.data['booking_id'] == 1

@pytest.mark.django_db
def test_booking_date_intersection():
    client=APIClient()
    url='/booking/create/'
    data={
        'room_id':1,
        'date_start':'2025-11-1',
        'date_end':'2025-11-7'
    }
    room1=Room.objects.create(description='room 1', price=8000)
    booking1=Booking.objects.create(room=room1, date_start='2025-11-5', date_end='2025-11-9')
    response=client.post(url, data, format='json')
    assert response.status_code == 400
    a=response.data
    assert 'room is already booked for the selected dates' in str(response.data['non_field_errors'])

@pytest.mark.django_db
def test_get_booking_for_room():
    client=APIClient()
    url='/booking/list/?room_id=1'
    room1=Room.objects.create(description='room 1', price=8000)
    booking1=Booking.objects.create(room=room1, date_start='2025-11-5', date_end='2025-11-9')
    booking2 = Booking.objects.create(room=room1, date_start='2025-12-5', date_end='2025-12-9')
    response=client.get(url)
    a=response.data
    assert response.status_code == 200
    assert len(response.data) == 2

@pytest.mark.django_db
def test_delete_booking():
    client=APIClient()
    room1=Room.objects.create(description='room 1', price=8000)
    booking1=Booking.objects.create(room=room1, date_start='2025-11-5', date_end='2025-11-9')
    a=booking1
    url=f'/booking/delete/{booking1.id}/'
    response=client.delete(url)
    assert response.status_code == 200
    b=booking1.id
    assert response.data['delete booking'] == booking1.id