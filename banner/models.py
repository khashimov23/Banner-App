from django.db import models
from django.contrib.auth.models import User





class Place_owner(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=13, null=True)

    def __str__(self) -> str:
        return self.name


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
    busy = models.CharField(max_length=200, default="Bo'sh", null=True, choices=BUSY)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    current_post = models.ForeignKey('Tadbirkor', null=True, blank=True ,on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.address



class Tadbirkor(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=13, null=True)
    info = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name




class Place_image(models.Model):
    image = models.ImageField(upload_to='images')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='place_images')
    time_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    class Meta:
        ordering = ['time_created'] 




class Order(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('NotActive', 'NotActive')
    )

    tadbirkor = models.ForeignKey(Tadbirkor, null=True, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, null=True, on_delete=models.CASCADE)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    status = models.CharField(max_length=100, default='Active', null=True, choices=STATUS)

    def __str__(self) -> str:
        return self.tadbirkor.name



    
