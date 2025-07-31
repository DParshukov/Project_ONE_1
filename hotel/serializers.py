from rest_framework import serializers
from .models import Room, Booking


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ["id", "price", "description", "created_at"]



    def to_representation(self, instance):
        if self.context.get('only_id'):
            return {'room':instance.id}
        return super().to_representation(instance)

class BookingSerializer(serializers.ModelSerializer):

    booking_id=serializers.IntegerField(source="id", read_only=True)
    room_id=serializers.PrimaryKeyRelatedField(queryset=Room.objects.all(),
                                               source="room", write_only=True )
    class Meta:
        model = Booking
        fields=["booking_id", "room_id", "date_start", "date_end"]

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
        if self.context.get('only_id'):
            return {"booking_id":instance.id}
        return super().to_representation(instance)