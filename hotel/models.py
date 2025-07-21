from django.db import models


class Room(models.Model):
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2 )
    creation_time=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=["id"]

    def __str__(self):
        return f"{self.id}"

class Booking(models.Model):
    date_start=models.DateField()
    date_end=models.DateField()
    creation_time=models.DateTimeField(auto_now_add=True)
    room=models.ForeignKey(Room,on_delete=models.CASCADE,related_name='bookings')

    class Meta:
        ordering=["date_start"]


    def __str__(self):
        return f"{self.date_start}:{self.date_end}"

