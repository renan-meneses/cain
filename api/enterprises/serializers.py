from rest_framework import serializers

from .models import EnterprisesModel


class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnterprisesModel
        fields = ["cnpj", "corporate", "fantasy", "associates"]
