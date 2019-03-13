from django.db import models

# Create your models here.
# class NewsLetterRecipients(models.Model):
#     name = models.CharField(max_length = 30)
#     email = models.EmailField()

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'images/')
    Bio = models.CharField(max_length =30)
    def __str__(self):
        return self.profile_photo

class Comments(models.Model):
    comment = models.CharField(max_length =30)
    # pub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment

class Image(models.Model):
    image_name = models.CharField(max_length =30)
    image_caption = models.CharField(max_length =30)
    # image_profile = models.ForeignKey(Profile)
    img_comments = models.ForeignKey(Comments)
    image = models.ImageField(upload_to = 'images/')
    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news

    def __str__(self):
        return self.image_name
