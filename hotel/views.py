from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Room, Booking
from .serializers import (
    RoomSerializer,
    RoomCreateSerializers,
    BookingSerializer,
    BookingCreateSerializers)


class RoomListView(APIView):
    def get(self,request):
        sort_by=request.GET.get("sort_by","creation_time")
        order=request.GET.get("order", "asc")
        if sort_by not in {"creation_time","price"}:
            return Response({"error": "invalid sort_by"}, status=400)
        ordering=sort_by if order == "asc" else f"-{sort_by}"
        rooms=Room.objects.all().order_by(ordering)
        data=RoomSerializer(rooms, many=True).data
        return Response(data, status=status.HTTP_200_OK)

class RoomCreateView(APIView):
    def post(self, request):
        serializer=RoomCreateSerializers(data=request.data)
        if serializer.is_valid():
            room=serializer.save()
            body=serializer.to_representation(room)

            return Response(body,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class RoomDeleteView(APIView):
    def delete(self, request, room_id:int):
        room=get_object_or_404(Room,pk=room_id)
        room.delete()
        return Response({f"detail": f"room deleted {room_id}"}, status=status.HTTP_200_OK)

class BookingListView(APIView):
    def get(self,request):
        try:
            room_id=request.GET["room_id"]

        except(KeyError,ValueError):
            return Response("error : room_id required ", status=400)
        queryset=Booking.objects.filter(room_id=room_id).order_by("date_start")
        data=BookingSerializer(queryset, many=True).data
        return Response(data, status=status.HTTP_200_OK)


class BookingCreateView(APIView):
    def post(self, request):
        serializer=BookingCreateSerializers(data=request.data)

        # print(f"!!!!!{serializer.initial_data}")
        if serializer.is_valid():
            # print(f"________{serializer.validated_data}")
            booking = serializer.save()
            # print(f"++++++++++{booking}")
            body=serializer.to_representation(booking)
            # print(f"==========={body}")
            return Response(body, status=status.HTTP_201_CREATED )

        else:
            # print(f"$$$$$$$$$$$${serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookingDeleteView(APIView):
    def delete(self, request, booking_id:int):
        booking=get_object_or_404(Booking, pk=booking_id)
        booking.delete()
        return Response({"delete booking":booking_id}, status=status.HTTP_200_OK)