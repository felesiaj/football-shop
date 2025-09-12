from django.db import models
import uuid

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Jersey', 'Jersey'),
        ('Shoes', 'Shoes'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    price = models.IntegerField()  # harga produk
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name