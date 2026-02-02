from django.db import models
from django.contrib.auth.models import User

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='equipment_images/')
    price_per_day = models.IntegerField()
    owner_contact = models.CharField(max_length=15)
    is_available = models.BooleanField(default=True)

    def __str__(self):       #!__str__() is a special method used to return a human-readable name of an object.
        return self.name
    
class RentalRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment,on_delete=models.CASCADE) 
    start_date = models.DateField()
    end_date= models.DateField()
    total_days = models.IntegerField()
    total_price= models.IntegerField()
    status = models.CharField(max_length=20,default="Pending")

    def __str__(self):
        return self.user.username


