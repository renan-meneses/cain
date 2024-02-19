from django.urls import path

from .views import CreateEmployment, ListEnterprise

urlpatterns = [
    path("enterprise/", ListEnterprise.as_view(), name="enterprise"),
    path("employment/", CreateEmployment.as_view(), name="employment"),
]
