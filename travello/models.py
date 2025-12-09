from django.db import models

# Create your models here.

# class Destination:
#     id: int
#     name: str
#     img: str
#     desc: str
#     price: int
#     offer: bool

class Destination(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    adults = models.PositiveIntegerField(default=1)
    children = models.PositiveIntegerField(default=0)
    start_date = models.DateField()
    end_date = models.DateField()
    contact_number = models.CharField(max_length=15)
    booked_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Booking by {self.name} for {self.destination.name}"