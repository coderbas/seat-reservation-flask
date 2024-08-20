from django.db import models

class Seat(models.Model):
    number = models.CharField(max_length=10)
    is_reserved = models.BooleanField(default=False)

    def __str__(self):
        return self.number

class Reservation(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"Reservation for {self.name} - Seat {self.seat.number}"