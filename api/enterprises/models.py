from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from api.utils.base_model import BaseModel

User = get_user_model()


class EnterprisesModel(BaseModel):
    cnpj = models.CharField(
        max_length=14, validators=[MinLengthValidator(14)], unique=True
    )
    corporate = models.CharField(max_length=150, unique=True)
    fantasy = models.CharField(max_length=150, unique=True)
    associates = models.ManyToManyField(User, related_name="work_for")
