from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Purchases, Sales, Product


@receiver(post_save, sender=Purchases)
def create_Purchases(sender, instance=None, created=False, **kwargs):
    if created:
        Product.objects.create(user=instance)
