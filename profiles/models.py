from django.db import models
from django.contrib.auth.models import User
from profiles.choices import profile
from cloudinary.models import CloudinaryField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pfp = CloudinaryField('image', blank=False, null=False, help_text="upload your  profile picture")
    image_1 = CloudinaryField('image', blank=False, null=False, help_text="upload your photo")
    image_2 = CloudinaryField('image', blank=False, null=False, help_text="upload your photo")
    year = models.CharField(max_length=4, choices=profile.YEAR_CHOICES, default="NONE")
    department = models.CharField(max_length=9, choices=profile.DEPARTMENT_CHOICES, default="NONE")
    living = models.CharField(max_length=11, choices=profile.LIVING_CHOICES, default="NONE")
    socities = models.CharField(max_length=11, choices=profile.SOCITIES_CHOICES, default="NONE")
    hangout = models.CharField(max_length=100)
    companionship = models.CharField(max_length=10, choices=profile.COMPANIONSHIP_CHOICES, default="NONE")
    routine = models.CharField(max_length=11, choices=profile.ROUTINE_CHOICES, default="NONE")
    activity = models.CharField(max_length=100)
    hobbies = models.CharField(max_length=17, choices=profile.HOBBIES_CHOICES, default="NONE")
    goal = models.CharField(max_length=16, choices=profile.GOAL_CHOICES, default="NONE")
    change = models.CharField(max_length=100)
    excuse = models.CharField(max_length=100)


    def __str__(self):
        return self.user.first_name