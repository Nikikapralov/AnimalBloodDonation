from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from Backend import settings
from Backend.custom_auth.models import CustomUser


class Owner(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}" if any([self.first_name,
                                                                                self.last_name,
                                                                                self.middle_name]) else str(self.user_id_fk)


class Pet(models.Model):
    name = models.CharField(max_length=50, default="Animal")
    age = models.IntegerField()
    photo = models.ImageField(upload_to="pet_images/")
    breed = models.CharField(max_length=50, default="Unknown")
    blood_type = models.CharField(max_length=10, default="Unknown")
    region = models.CharField(max_length=50, default="Not specified")
    description = models.CharField(max_length=500)
    is_deleted = models.BooleanField(default=False)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Case(models.Model):
    request_blood = models.BooleanField(default=False)
    donate_blood = models.BooleanField(default=True)
    description = models.CharField(max_length=500)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    cover_photo = models.ImageField(null=True)

    def __str__(self):
        return "Case"


class CaseImage(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="case_images/")
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return "Image"


class Comment(models.Model):
    text_comment = models.CharField(max_length=500)
    sender = models.ForeignKey(Owner, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)

    def __str__(self):
        return "Comment"


class Message(models.Model):
    text_message = models.CharField(max_length=500)

    def __str__(self):
        return "Message"


class PrivateMessageTable(models.Model):
    sender = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="sender")
    recipient = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="recipient")
    message = models.ForeignKey(Message, on_delete=models.CASCADE)

    def __str__(self):
        return "PrivateMessageTable"

