from django.db import models

# Create your models here.

from Backend.auth.models import CustomUser


class Owner(models.Model):
    user_id_fk = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)


class Pet(models.Model):
    name = models.CharField(max_length=50, default="Animal")
    age = models.IntegerField()
    photo = models.ImageField(upload_to="pet_images/")
    breed = models.CharField(max_length=50, default="Unknown")
    blood_type = models.CharField(max_length=10, default="Unknown")
    region = models.CharField(max_length=50, default="Not specified")
    description = models.CharField(max_length=500)
    is_deleted = models.BooleanField(default=False)
    owner_id_fk = models.ForeignKey(Owner, on_delete=models.CASCADE)


class Case(models.Model):
    request_blood = models.BooleanField(default=False)
    donate_blood = models.BooleanField(default=True)
    description = models.CharField(max_length=500)
    pet_id_fk = models.ForeignKey(Pet, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)


class CaseImage(models.Model):
    case_id_fk = models.ForeignKey(Case, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="case_images/")
    is_deleted = models.BooleanField(default=False)


class Comment(models.Model):
    text_comment = models.CharField(max_length=500)
    is_deleted = models.BooleanField(default=False)
    case_id_fk = models.ForeignKey(Case, on_delete=models.CASCADE)


class Message(models.Model):
    text_message = models.CharField(max_length=500)


class PrivateMessageTable(models.Model):
    sender_id_fk = models.ForeignKey(Owner, on_delete=models.CASCADE)
    recipient_id_fk = models.ForeignKey(Owner, on_delete=models.CASCADE)
    message_id_fk = models.ForeignKey(Message, on_delete=models.CASCADE)

