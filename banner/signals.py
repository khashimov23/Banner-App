from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Order, Place


@receiver(post_save, sender=Order)
def change_status(sender, instance, created, *args, **kwargs):
    if created:
        instance.place.busy = 'Band'
        instance.place.save()


