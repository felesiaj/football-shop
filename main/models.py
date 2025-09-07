from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()  # harga produk
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title