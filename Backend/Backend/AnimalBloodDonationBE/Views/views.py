
# Create your views here.
import rest_framework.generics as drf
from django.http import Http404

from Backend.Serializers.ABD_serializers.get_full_data_admin import \
    CaseImageSerializer, CommentSerializer, CaseSerializerDeep
from Backend.AnimalBloodDonationBE.models import Case, CaseImage, Comment
from Backend.Mixins.REST_mixins.dynamic_fields import DynamicFieldsHelper


class GetAllCases(DynamicFieldsHelper, drf.ListAPIView):
    serializer_class = CaseSerializerDeep
    queryset = Case.objects.filter(is_deleted=False)


class GetSpecificCase(DynamicFieldsHelper, drf.ListAPIView):
    serializer_class = CaseSerializerDeep

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








