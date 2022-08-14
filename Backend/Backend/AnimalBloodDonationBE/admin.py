from django.contrib import admin

# Register your models here
from Backend.AnimalBloodDonationBE.models import PrivateMessageTable, Message, Comment, Case, Owner, CaseImage, Pet


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    pass

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    pass

@admin.register(CaseImage)
class CaseImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass

@admin.register(PrivateMessageTable)
class PrivateMessageTableAdmin(admin.ModelAdmin):
    pass

