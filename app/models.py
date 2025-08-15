from django.db import models

# Create your models here.
class GeneralInfo(models.Model):
    company_name = models.CharField(max_length=255, default='Company')
    location = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    opening_hours = models.CharField(max_length=100, default='9 AM - 5 PM', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.company_name
