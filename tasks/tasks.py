# myapp/tasks.py
from datetime import timedelta
from urllib import response

from celery import shared_task
from django.utils import timezone

from api.enterprises.models import EnterprisesModel
from api.utils.requests import get_data_from_endpoint


@shared_task
def TaskreceitaFederal():
    enterprises = EnterprisesModel.objects.all()
    for enterprise in enterprises:
        if timezone.now() - enterprise.created_at >= timedelta(days=30):
            url = "https://receitaws.com.br/v1/cnpj/" + enterprise.cnpj
            reponser = get_data_from_endpoint(url)
            if response:
                enterprise.fantasy = reponser["fantasia"]
                enterprise.corporate = reponser["nome"]
                enterprise.situation = response["situacao"]
                enterprise.save()
    print("verified by the IRS!")


TaskreceitaFederal()
