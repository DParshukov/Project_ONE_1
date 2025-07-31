from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.shortcuts import get_object_or_404

from .models import Room, Booking
from .serializers import (
    RoomSerializer,

    BookingSerializer)


class RoomView(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def list(self, request, *args, **kwargs):
        sort_by=request.GET.get("sort_by","created_at")
        order=request.GET.get("order", "asc")
        if sort_by not in {"created_at","price"}:
            return Response({"error": "invalid sort_by"}, status=400)
        ordering=sort_by if order == "asc" else f"-{sort_by}"
        rooms=Room.objects.all().order_by(ordering)
        data=RoomSerializer(rooms, many=True).data
        return Response(data, status=status.HTTP_200_OK)


    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        room=serializer.save()
        return Response(RoomSerializer(room, context={'only_id':True}).data,status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        room_id = instance.id
        self.perform_destroy(instance)
        return Response({f"detail": f"room deleted {room_id}"}, status=status.HTTP_200_OK)


class BookingView(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def list(self, request, *args, **kwargs):
        try:
            room_id=request.GET["room_id"]

        except(KeyError,ValueError):
            return Response("error : room_id required ", status=400)
        queryset=Booking.objects.filter(room_id=room_id).order_by("date_start")
        data=BookingSerializer(queryset, many=True).data
        return Response(data, status=status.HTTP_200_OK)


    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        booking = serializer.save()
        return Response( BookingSerializer(booking, context={'only_id':True}).data, status=status.HTTP_201_CREATED )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        booking_id = instance.id
        self.perform_destroy(instance)
        return Response({"delete booking":booking_id}, status=status.HTTP_200_OK)


