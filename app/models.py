from django.db import models
from django.utils import timezone

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

class service(models.Model):
    icon = models.CharField(max_length=100, null=True, blank=True)
    tittle = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.tittle
    

class Testimonial(models.Model):
    user_image = models.CharField(max_length=255, null=True, blank=True)
    star_count = [
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
        (4, 'Four'),
        (5, 'Five'),
    ]
    rating_count = models.IntegerField(choices=star_count)
    username = models.CharField(max_length=100)
    user_job = models.CharField(max_length=100)
    review = models.TextField()

    def __str__(self):
        return f"{self.username} - {self.user_job}"


class FrequentlyAskedQuestion(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question

class ContactFormLog(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    action_time = models.DateTimeField(null=True, blank=True)
    is_success = models.BooleanField(default=False)
    is_error = models.BooleanField(default=False)
    error_message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.email

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    joined_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Blog(models.Model):
    blog_image = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title