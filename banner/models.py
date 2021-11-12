from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser


class Place_owner(AbstractUser):
    phone = models.CharField(verbose_name='Telefon', max_length=13, null=True, unique=False)



class Place(models.Model):
    BUSY = (
        ('Band','Band'),
        ("Bo'sh","Bo'sh"),
    )
    owner = models.ForeignKey(Place_owner, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='images', null=True)
    image2 = models.ImageField(upload_to='images', null=True, blank=True)
    image3 = models.ImageField(upload_to='images', null=True, blank=True)
    busy = models.CharField(max_length=200, default="Bo'sh", choices=BUSY)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    boglangan_tadbirkor = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.owner.username}ning - {self.address}dagi joyi"




class Tadbirkor(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=13, null=True)
    info = models.CharField(max_length=200)


    def __str__(self) -> str:
        return self.name



class Order(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('NotActive', 'NotActive')
    )

    tadbirkor = models.ForeignKey(Tadbirkor, null=True, on_delete=models.DO_NOTHING)
    place = models.ForeignKey(Place, limit_choices_to={'busy':"Bo'sh"}, null=True, on_delete=models.DO_NOTHING)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    status = models.CharField(max_length=100, default='Active', null=True, choices=STATUS)


    def __str__(self) -> str:
        return f"{self.tadbirkor.name} ning ({self.place.address}) ga bog'langan"