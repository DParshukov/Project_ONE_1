"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hotel.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rooms/list/', RoomListView.as_view(), name="rooms_list" ),
    path('room/create/',RoomCreateView.as_view(),name="room_create"),
    path('room/delete/<int:room_id>/',RoomDeleteView.as_view(),name="room_delete"),
    path('booking/list/', BookingListView.as_view(), name="booking_list"),
    path('booking/create/', BookingCreateView.as_view(), name="booking_create"),
    path('booking/delete/<int:booking_id>/', BookingDeleteView.as_view(), name="booking_delete")

]
