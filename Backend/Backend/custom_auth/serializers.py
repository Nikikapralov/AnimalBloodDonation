

from Backend.Serializers.DynamicFields import DynamicFieldsModelSerializer
from Backend.custom_auth.models import CustomUser


class CustomUserSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = CustomUser
        fields = "__all__"
