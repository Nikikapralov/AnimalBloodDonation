
# Create your views here.
import rest_framework.generics as drf
from django.http import Http404
from rest_framework.permissions import IsAdminUser

from Backend.AnimalBloodDonationBE.ABD_serializers.get_full_data_admin import OwnerSerializer, PetSerializer, CaseSerializer, \
    CaseImageSerializer, CommentSerializer, MessageSerializer, PrivateMessageTableSerializer
from Backend.AnimalBloodDonationBE.models import Owner, Pet, Case, CaseImage, Comment, Message, PrivateMessageTable
from Backend.Mixins.REST_mixins.dynamic_fields import DynamicFieldsHelper


class GetAllOwnersAdmin(DynamicFieldsHelper, drf.ListAPIView):
    serializer_class = OwnerSerializer
    queryset = Owner.objects.all()
    permission_classes = [IsAdminUser]


class GetAllPetsAdmin(DynamicFieldsHelper, drf.ListAPIView):
    serializer_class = PetSerializer
    queryset = Pet.objects.all()
    permission_classes = [IsAdminUser]


class GetAllCommentsAdmin(DynamicFieldsHelper, drf.ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAdminUser]


class GetAllCasesAdmin(DynamicFieldsHelper, drf.ListAPIView):
    serializer_class = CaseSerializer
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






class GetAllCases(DynamicFieldsHelper, drf.ListAPIView):
    serializer_class = CaseSerializer
    queryset = Case.objects.filter(is_deleted=False)


class GetSpecificCase(DynamicFieldsHelper, drf.ListAPIView):
    serializer_class = CaseSerializer

    def get_queryset(self):
        specific_case = Case.objects.filter(pk=self.kwargs["pk"])
        if not specific_case:
            raise Http404
        return specific_case


class GetAllCurrentCaseImages(DynamicFieldsHelper, drf.ListAPIView):
    serializer_class = CaseImageSerializer

    def get_queryset(self):
        all_images = CaseImage.objects.filter(case_id_fk=self.kwargs["pk"], is_deleted=False)
        return all_images


class GetAllCurrentCaseComments(DynamicFieldsHelper, drf.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        all_comments = Comment.objects.filter(case_id_fk=self.kwargs["pk"], is_deleted=False)
        return all_comments








