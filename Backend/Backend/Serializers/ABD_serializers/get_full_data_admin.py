from rest_framework import serializers
from rest_framework.utils.serializer_helpers import ReturnList, ReturnDict

from Backend.Serializers.ABD_serializers.common import CaseImageSerializer, CommentSerializer,\
    PrivateMessageTableSerializer
from Backend.AnimalBloodDonationBE.models import Owner, PrivateMessageTable, Comment, CaseImage, Case, Pet
from Backend.Serializers.DynamicFields import DynamicFieldsModelSerializer
from Backend.Serializers.utils.funcs import get_sender, get_recipient
from Backend.custom_auth.models import CustomUser
from Backend.custom_auth.serializers import CustomUserSerializer


class PetSerializerDeep(DynamicFieldsModelSerializer):
    """
    PetSerializerDeep to get all pets and their respective relations.
    """
    cases = serializers.SerializerMethodField()

    class Meta:
        model = Pet
        exclude = ("is_deleted", )

    @staticmethod
    def get_cases(obj: Case) -> ReturnList:
        """
        Get all cases.
        @param obj: Case.
        @return: Instance of ReturnList with instances of ReturnDict for each Case entry.
        """
        case = Case.objects.filter(pet=obj.pk)
        serializer = CaseSerializerDeep(case, many=True)
        return serializer.data



class CaseSerializerDeep(DynamicFieldsModelSerializer):
    """
    CaseSerializerDeep to get all cases and their respective relations.
    """
    case_images = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Case
        exclude = ("is_deleted", )

    @staticmethod
    def get_case_images(obj: Case) -> ReturnList:
        """
        Gets all the case images and their respective relations.
        @param obj: Case.
        @return: Returns an instance of ReturnList object that has instances of ReturnDict in it as serialized data.
        """
        case_images = CaseImage.objects.filter(case=obj.pk)
        serializer = CaseImageSerializer(case_images, many=True)
        return serializer.data

    @staticmethod
    def get_comments(obj: Case) -> ReturnList:
        """
        Gets all comments and their respective relations. Adds the author of the comment (as sender)
        to the serialized data.
        @param obj: Case.
        @return: Returns a ReturnList instance with ReturnDict instances for each comment as serialized data.
        """
        comments = Comment.objects.filter(case=obj.pk)
        serializer_data = CommentSerializer(comments, many=True).data
        for entry in serializer_data:
            sender = get_sender(entry, Owner, "sender")
            entry["sender"] = sender
        return serializer_data


class OwnerSerializerDeep(DynamicFieldsModelSerializer):
    """
    OwnerSerializerDeep to get all the Owners and their respective relations.
    """

    pets = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    messages = serializers.SerializerMethodField()

    class Meta:
        model = Owner
        exclude = ("is_deleted", )
        depth = 10

    @staticmethod
    def get_pets(obj: Owner) -> ReturnList:
        """
        Gets all the pets and their respective deep relations.
        @param obj: Owner.
        @return: Returns a ReturnList of serialized ReturnDict data.
        """
        pets = Pet.objects.filter(owner=obj.pk)
        serializer = PetSerializerDeep(pets, many=True)
        return serializer.data

    @staticmethod
    def get_user(obj: Owner) -> ReturnDict:
        """
        Gets all users and their respective deep relations. Shows only email as the rest is confidential data.
        @param obj: Owner.
        @return: Returns a ReturnDict object of serialized data.
        """
        user = CustomUser.objects.get(pk=obj.pk)
        serializer = CustomUserSerializer(user, fields=["email"])
        return serializer.data

    @staticmethod
    def get_messages(obj: Owner) -> dict:
        """
        Gets all messages and their respective sender and recipient.
        @param obj: Owner.
        @return: Returns an instance of dict object of serialized data with added sender and recipient.
        """
        message_table = PrivateMessageTable.objects.filter(recipient=obj.pk)
        result = {}
        for table in message_table:
            data_dict = PrivateMessageTableSerializer(table).data
            data_dict["sender"] = get_sender(data_dict, Owner, "sender")
            data_dict["recipient"] = get_recipient(data_dict, Owner, "recipient")
            result.update(data_dict)
        return result

