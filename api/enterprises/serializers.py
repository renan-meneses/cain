from rest_framework import serializers

from .models import EnterprisesModel


class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnterprisesModel
        fields = ["cnpj", "corporate", "fantasy", "associates"]


class EmploymentSerializer(serializers.Serializer):
    enterprises = serializers.CharField()  # noaq: F811
    employment = serializers.CharField()
