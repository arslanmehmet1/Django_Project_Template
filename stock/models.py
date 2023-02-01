from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Category(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'


class Brand(models.Model):
    name=models.CharField(max_length=30)
    image=models.ImageField(upload_to="pictures", default="resim.png")

    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    name=models.CharField(max_length=30)
    category=models.ForeignKey(Category, on_delete=models.PROTECT, related_name='category')
    brand=models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='brand')
    stock=models.SmallIntegerField()
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.brand}'

class Sales(models.Model):
    user=models.ForeignKey(User, on_delete=models.PROTECT)
    product=models.ForeignKey(Product, on_delete=models.PROTECT)
    brand=models.ForeignKey(Brand, on_delete=models.PROTECT)
    quantity=models.SmallIntegerField()
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        validators=[MinValueValidator(1)]
    )
    def __str__(self):
        return f'{self.user} {self.product} {self.brand}'

class Firms(models.Model):
    name=models.CharField(max_length=40)
    phone=models.CharField(max_length=40)
    address=models.CharField(max_length=40)
    image=models.ImageField(upload_to="pictures", default="resim.png")

    def __str__(self):
        return f'{self.name} {self.image}'

class Purchases(models.Model):
    user=models.ForeignKey(User, on_delete=models.PROTECT)
    firm=models.ForeignKey(Firms, on_delete=models.PROTECT)
    brand=models.ForeignKey(Brand, on_delete=models.PROTECT)
    product=models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity=models.SmallIntegerField()
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        validators=[MinValueValidator(1)]
    )

    def __str__(self):
        return f'{self.user} {self.firm} {self.brand}'


