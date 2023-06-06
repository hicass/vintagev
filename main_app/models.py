from django.db import models
from django.contrib.auth.models import User




CATEGORIES = (
  ('T', 'Top'),
  ('Btm', 'Bottom'),
  ('Jckt', 'Jacket'),
  ('Drs', 'Dress'),
  ('Jmp', 'Jumpsuit'),
  ('Sh', 'Shoes'),
  ('Acc', 'Accessory')
)

SIZES = (
  ('XL', 'Xtra Large'),
  ('L', 'Large'),
  ('M', 'Medium'),
  ('S', 'Small'),
  ('XS', 'Xtra Small')
)

CONDITION = (
  ('Bn', 'Brand New'),
  ('Ln', 'Like New'),
  ('UE', 'USED - Excellent'),
  ('UG', 'USED - Good'),
  ('UF', 'USED - Fair')
)


# Create your models here.
class Clothes(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  category = models.CharField(
    max_length=20,
    choices=CATEGORIES,
    default=[0][0]
    )
  size = models.CharField(
    max_length=20,
    choices=SIZES,
    default=[0][0]
    )
  condition = models.CharField(
    max_length=20,
    choices=CONDITION,
    default=[0][0]
    )
  material = models.CharField(max_length=100)
  color = models.CharField(max_length=100)
  price= models.IntegerField()
  brand = models.CharField(max_length=100)
  likes = models.IntegerField()
  clothing_name = models.CharField(max_length=100)
  description = models.TextField(max_length=200)
