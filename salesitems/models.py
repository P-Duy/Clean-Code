from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class SalesItem(models.Model):
    user_account_id = models.BinaryField()
    name = models.CharField(max_length=512)
    price = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(2147483647)]
    )