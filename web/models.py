from django.db import models
from versatileimagefield.fields import VersatileImageField
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50, default='')
    email = models.EmailField()
    comment = models.TextField()

    def __str__(self):
        return self.name
    
class Product(models.Model):
    product_name = models.CharField(max_length=50, default='')
    product_price  = models.CharField(max_length=50, default='')
    product_tag = models.CharField(max_length=50, default='')
    product_image = VersatileImageField('Photo',blank=True,null=True,upload_to="product/")
    product_image_left= VersatileImageField('product_image_left',blank=True,null=True,upload_to="product/")
    product_image_right= VersatileImageField('product_image_right',blank=True,null=True,upload_to="product/")
    product_image_back= VersatileImageField('product_image_back',blank=True,null=True,upload_to="product/")
    product_detail = models.TextField()
    def __str__(self):
        return self.product_name
    