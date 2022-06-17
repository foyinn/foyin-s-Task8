from django.db import models

class HotelRecord(models.Model):
    Name = models.CharField(max_length=1000)
    Email = models.EmailField()
    Occupation = models.CharField(max_length=1000)
    Room_Number = models.IntegerField()
    Amount_Paid = models.DecimalField(max_digits=10, decimal_places=2)
    Number_Of_Nights = models.IntegerField()
    Day_Of_Arrival =models.DateField()
    Day_Of_Departure = models.DateField()

    def __str__(self):
        return self.Name
