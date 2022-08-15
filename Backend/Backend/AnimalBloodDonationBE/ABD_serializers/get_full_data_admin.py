from rest_framework import serializers

from Backend.AnimalBloodDonationBE.ABD_serializers.common import CaseImageSerializer, CommentSerializer,\
    PrivateMessageTableSerializer
from Backend.AnimalBloodDonationBE.models import Owner, PrivateMessageTable, Comment, CaseImage, Case, Pet
from Backend.Serializers.DynamicFields import DynamicFieldsModelSerializer
from Backend.custom_auth.models import CustomUser
from Backend.custom_auth.serializers import CustomUserSerializer


class PetSerializerDeep(DynamicFieldsModelSerializer):
    cases = serializers.SerializerMethodField()

    class Meta:
        model = Pet
        exclude = ("is_deleted", )

    def get_cases(self, obj):
        case = Case.objects.filter(pet=obj.pk)
        serializer = CaseSerializerDeep(case, many=True)
        return serializer.data



class CaseSerializerDeep(DynamicFieldsModelSerializer):
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
        serializer_data = CommentSerializer(comments, many=True).data[0]
        sender = serializer_data["sender"]
        sender_name = Owner.objects.get(pk=sender).__str__()
        serializer_data["sender"] = sender_name
        return serializer_data



class OwnerSerializerDeep(DynamicFieldsModelSerializer):

    pets = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    messages = serializers.SerializerMethodField()

    class Meta:
        model = Owner
        exclude = ("is_deleted", )
        depth = 10

    def get_pets(self, obj):
        pets = Pet.objects.filter(owner=obj.pk)
        serializer = PetSerializerDeep(pets, many=True)
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
            data_dict["sender"] = Owner.objects.get(pk=data_dict["sender"]).__str__()
            data_dict["recipient"] = Owner.objects.get(pk=data_dict["recipient"]).__str__()
            result.update(data_dict)

        return result
