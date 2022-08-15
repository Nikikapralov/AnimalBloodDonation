from rest_framework import serializers

from Backend.AnimalBloodDonationBE.models import CaseImage, Comment, Message, PrivateMessageTable
from Backend.Serializers.DynamicFields import DynamicFieldsModelSerializer


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