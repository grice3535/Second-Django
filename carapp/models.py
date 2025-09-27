from django.db import models

# Create your models here.
class Car(models.Model):
    FUEL_TYPE = [
        ('gas', 'Gas'),
        ('diesel', 'Diesel'),
        ('hybrid', 'Hybrid'),
        ('lp_gas', 'LP Gas')
    ]

    ROOF_TYPE = [
        ('solid', 'Solid'),
        ('sunroof', 'Sunroof'),
        ('convertible', 'Convertible')
    ]
    vin = models.CharField(max_length=50)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    color = models.CharField(max_length=25)
    door_num = models.IntegerField()
    roof_type = models.CharField(choices=ROOF_TYPE, default='solid')
    year = models.SmallIntegerField()
    fuel_type = models.CharField(choices=FUEL_TYPE, default='gas')

    def __str__(self):
        return f"{self.color} {self.make} {self.model}"