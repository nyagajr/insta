from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_photo = models.CharField(max_length =30)
    Bio = models.CharField(max_length =30)

class Comments(models.Model):
    comment = models.CharField(max_length =30)

class Image(models.Model):
    image = models.CharField(max_length =30)
    image_name = models.CharField(max_length =30)
    image_caption = models.CharField(max_length =30)
    image_profile = models.ForeignKey(Profile)
    img_comments = models.ForeignKey(Comments)
