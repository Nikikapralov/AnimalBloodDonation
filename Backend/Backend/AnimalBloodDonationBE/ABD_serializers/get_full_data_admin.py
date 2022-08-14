from rest_framework import serializers

from Backend.AnimalBloodDonationBE.models import Owner, PrivateMessageTable, Message, Comment, CaseImage, Case, Pet
from Backend.Serializers.DynamicFields import DynamicFieldsModelSerializer
from Backend.custom_auth.models import CustomUser
from Backend.custom_auth.serializers import CustomUserSerializer


class PetSerializer(DynamicFieldsModelSerializer):
    cases = serializers.SerializerMethodField()

    class Meta:
        model = Pet
        exclude = ("is_deleted", )

    def get_cases(self, obj):
        case = Case.objects.filter(pet=obj.pk)
        serializer = CaseSerializer(case, many=True)
        return serializer.data



class CaseSerializer(DynamicFieldsModelSerializer):
    case_images = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Case
        exclude = ("is_deleted", )

    def get_case_images(self, obj):
        case_images = CaseImage.objects.filter(case=obj.pk)
        serializer = CaseImageSerializer(case_images, many=True)
        return serializer.data

    def get_comments(self, obj):
        comments = Comment.objects.filter(case=obj.pk)
        serializer = CommentSerializer(comments, many=True)
        return serializer.data



class CaseImageSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = CaseImage
        exclude = ("is_deleted", )


class CommentSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Comment
        exclude = ("is_deleted", )


class MessageSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Message
        fields = "__all__"


class PrivateMessageTableSerializer(DynamicFieldsModelSerializer):
    message = serializers.SerializerMethodField()

    class Meta:
        model = PrivateMessageTable
        fields = "__all__"

    def get_message(self, obj):
        private_message = Message.objects.get(pk=obj.pk)
        serializer = MessageSerializer(private_message)
        return serializer.data


class OwnerSerializer(DynamicFieldsModelSerializer):

    pets = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    messages = serializers.SerializerMethodField()

    class Meta:
        model = Owner
        exclude = ("is_deleted", )
        depth = 10

    def get_pets(self, obj):
        pets = Pet.objects.filter(owner=obj.pk)
        serializer = PetSerializer(pets, many=True)
        return serializer.data

    def get_user(self, obj):
        user = CustomUser.objects.get(pk=obj.pk)
        serializer = CustomUserSerializer(user, fields=["email"])
        return serializer.data

    def get_messages(self, obj):
        message_table = PrivateMessageTable.objects.filter(recipient=obj.pk)
        result = {}
        for table in message_table:
            data_dict = PrivateMessageTableSerializer(table).data
            result.update(data_dict)

        return result
