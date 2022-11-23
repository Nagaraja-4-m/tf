from django.db import models
import os

# Create your models here.

# class SocialPlotform(models.Model):
#     d=models.AutoField(primary_key=True)
#     platform=models.EmailField(unique=True)

def filepath(request,filename):
    return os.path.join('core_app/static/img/', filename)

class SocialMedia(models.Model):
    id=models.AutoField(primary_key=True)
    platform=models.CharField(max_length=64,unique=True)
    title=models.CharField(max_length=256)
    url=models.URLField()
    status=models.SmallIntegerField(default=1)
    logo=models.ImageField(upload_to=filepath)
    filename=models.CharField( max_length=1080)
    updated_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='socialmedia'

class Contact(models.Model):
    id=models.AutoField(primary_key=True)
    type=models.CharField(max_length=64,unique=True)
    title=models.CharField(max_length=256)
    url=models.URLField()
    status=models.SmallIntegerField(default=1)
    logo=models.ImageField(upload_to=filepath)
    filename=models.CharField( max_length=1080)
    address=models.CharField(max_length=256)
    map_location=models.CharField(max_length=2048)
    map_location_iframe=models.CharField(max_length=2048)
    updated_at=models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table='contanct'

class ProductCard(models.Model):
    id=models.AutoField(primary_key=True)
    # type=models.CharField(max_length=64)
    heighliter=models.CharField(max_length=128)
    title=models.CharField(max_length=256)
    status=models.SmallIntegerField(default=1)
    filename=models.CharField( max_length=1080)
    img=models.ImageField(upload_to=filepath)
    updated_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='product_card'         

class SiteData(models.Model):
    id=models.AutoField(primary_key=True)
    status=models.SmallIntegerField(default=1)
    logo=models.ImageField(upload_to=filepath)
    logofilename=models.CharField( max_length=1080)
    banner=models.ImageField(upload_to=filepath)
    bannerfilename=models.CharField( max_length=1080)
    about_us=models.ImageField(upload_to=filepath)
    about_usfilename=models.CharField( max_length=1080)
    updated_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='site_data'         