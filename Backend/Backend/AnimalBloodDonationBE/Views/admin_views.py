import rest_framework.generics as drf
from django.http import Http404
from rest_framework.permissions import IsAdminUser

from Backend.AnimalBloodDonationBE.ABD_serializers.common import MessageSerializer
from Backend.AnimalBloodDonationBE.ABD_serializers.get_full_data_admin import \
    CaseImageSerializer, CommentSerializer, PrivateMessageTableSerializer, OwnerSerializerDeep, PetSerializerDeep, \
    CaseSerializerDeep
from Backend.AnimalBloodDonationBE.models import Owner, Pet, Case, CaseImage, Comment, Message, PrivateMessageTable
from Backend.Mixins.REST_mixins.dynamic_fields import DynamicFieldsHelper


class GetAllOwnersAdmin(DynamicFieldsHelper, drf.ListAPIView):
    serializer_class = OwnerSerializerDeep
    queryset = Owner.objects.all()
    permission_classes = [IsAdminUser]


class GetAllPetsAdmin(DynamicFieldsHelper, drf.ListAPIView):
    serializer_class = PetSerializerDeep
    queryset = Pet.objects.all()
    permission_classes = [IsAdminUser]


class GetAllCommentsAdmin(DynamicFieldsHelper, drf.ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAdminUser]


class GetAllCasesAdmin(DynamicFieldsHelper, drf.ListAPIView):
    serializer_class = CaseSerializerDeep
    queryset = Case.objects.all()
    permission_classes = [IsAdminUser]


class GetAllCaseImagesAdmin(DynamicFieldsHelper, drf.ListAPIView):
    serializer_class = CaseImageSerializer
    queryset = CaseImage.objects.all()
    permission_classes = [IsAdminUser]


class GetAllMessagesAdmin(DynamicFieldsHelper, drf.ListAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    permission_classes = [IsAdminUser]


class GetAllPrivateMessageTablesAdmin(DynamicFieldsHelper, drf.ListAPIView):
    serializer_class = PrivateMessageTableSerializer
    queryset = PrivateMessageTable.objects.all()
    permission_classes = [IsAdminUser]
