from rest_framework.serializers import ModelSerializer

from Backend.AnimalBloodDonationBE.models import Owner, PrivateMessageTable, Message, Comment, CaseImage, Case, Pet


class OwnerSeriliazer(ModelSerializer):
    model = Owner

    class Meta:
        fields = "__all__"


class PetSeriliazer(ModelSerializer):
    model = Pet

    class Meta:
        fields = "__all__"


class CaseSeriliazer(ModelSerializer):
    model = Case

    class Meta:
        fields = "__all__"


class CaseImageSeriliazer(ModelSerializer):
    model = CaseImage

    class Meta:
        fields = "__all__"


class CommentSeriliazer(ModelSerializer):
    model = Comment

    class Meta:
        fields = "__all__"


class MessageSeriliazer(ModelSerializer):
    model = Message

    class Meta:
        fields = "__all__"


class PrivateMessageTableSeriliazer(ModelSerializer):
    model = PrivateMessageTable

    class Meta:
        fields = "__all__"