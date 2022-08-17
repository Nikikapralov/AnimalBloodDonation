from rest_framework import serializers
from rest_framework.utils.serializer_helpers import ReturnDict

from Backend.AnimalBloodDonationBE.models import CaseImage, Comment, Message, PrivateMessageTable
from Backend.Serializers.DynamicFields import DynamicFieldsModelSerializer


class CaseImageSerializer(DynamicFieldsModelSerializer):
    """
    CaseImageSerializer to get all the images of a single case.
    """

    class Meta:
        model = CaseImage
        exclude = ("is_deleted", )


class CommentSerializer(DynamicFieldsModelSerializer):
    """
    CommentSerializer to get the comment that was exchanged.
    """

    class Meta:
        model = Comment
        exclude = ("is_deleted", )


class MessageSerializer(DynamicFieldsModelSerializer):
    """
    MessageSerializer to get the message that was exchanged.
    """

    class Meta:
        model = Message
        fields = "__all__"


class PrivateMessageTableSerializer(DynamicFieldsModelSerializer):
    """
    PrivateMessageTableSerializer to get the data for sender, recipient and the message that was sent.
    """
    message = serializers.SerializerMethodField()

    class Meta:
        model = PrivateMessageTable
        fields = "__all__"

    @staticmethod
    def get_message(obj: PrivateMessageTable) -> ReturnDict:
        """
        Gets the message from the private message table's key and the message table.
        @param obj: PrivateMessageTable Object
        @return: Returns OrderedDict as serialized data.
        """
        serializer = MessageSerializer(obj.message)
        return serializer.data
