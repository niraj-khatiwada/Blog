from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=255, blank=True, null=True)
    profile_image = models.ImageField(
        upload_to="accounts/profile_image", default="default.jpg", blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self):
        super().save()
        image = Image.open(self.profile_image.path)
        if (image.height > 300 and image.width > 300):
            output_size = (300, 300)
            image.thumbnail(output_size)
            image.save(self.profile_image.path)
