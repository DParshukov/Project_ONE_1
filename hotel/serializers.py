from rest_framework import serializers
from .models import Room, Booking


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ["id", "price", "description", "creation_time"]

class RoomCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields=["description","price"]


    def to_representation(self, instance):
        return {"room":instance.id}

class BookingSerializer(serializers.ModelSerializer):

    booking_id=serializers.IntegerField(source="id")


    class Meta:
        model = Booking
        fields=["booking_id", "date_start", "date_end"]

class BookingCreateSerializers(serializers.ModelSerializer):

    room_id=serializers.PrimaryKeyRelatedField(queryset=Room.objects.all(),
                                               source="room")
    class Meta:
        model = Booking
        fields=["room_id", "date_start", "date_end"]

    def validate(self, data):
        date_start=data["date_start"]
        date_end=data["date_end"]
        room=data['room']

        if date_end <= date_start :
            raise serializers.ValidationError({
                "date_end": "date_end must be greater than date_start"})

        intersection=Booking.objects.filter(room=room,
                                            date_start__lt=date_end,
                                            date_end__gt=date_start,).exists()
        if intersection:
            raise serializers.ValidationError({"room is already booked for the selected dates"})

        return data
    def to_representation(self, instance):
        return {"booking_id":instance.id}