from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from ..accounts.serializers import ListEmployment, User
from .models import EnterprisesModel
from .serializers import EmploymentSerializer, EnterpriseSerializer


class ListEnterprise(generics.GenericAPIView):
    queryset = EnterprisesModel.objects.all()
    serializer_class = EnterpriseSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            queryset = EnterprisesModel.objects.filter(associates=request.user)
            serialize = EnterpriseSerializer(queryset, many=True)
            return Response(serialize.data, status=status.HTTP_200_OK)
        except Exception as e:
            response = {"erro": str(e)}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        try:
            data = {}
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                enterprise = serializer.save()
                data["response"] = "Registration Successful!"
                data["enterprise"] = str(enterprise.fantasy)
                data["cnpj"] = str(enterprise.cnpj)

            return Response(data, status=status.HTTP_201_CREATED)
        except Exception as e:
            response = {"erro": str(e)}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class CreateEmployment(generics.GenericAPIView):
    queryset = EnterprisesModel.objects.all()
    serializer_class = EmploymentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            queryset = get_object_or_404(
                EnterprisesModel, id=request.query_params["enterprise"]
            )
            serialize = ListEmployment(queryset.associates.all(), many=True)
            return Response(serialize.data, status=status.HTTP_200_OK)
        except Exception as e:
            response = {"erro": str(e)}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        try:
            data = {}
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                employment = User.objects.get(id=request.data["employment"])
                enterprise = EnterprisesModel.objects.get(
                    id=request.data["enterprises"]
                )
                enterprise.associates.add(employment)
                enterprise.save()

                data["response"] = "Registration Successful!"
                data["enterprise"] = str(enterprise.fantasy)
                data["cnpj"] = str(enterprise.cnpj)

            return Response(data, status=status.HTTP_201_CREATED)
        except Exception as e:
            response = {"erro": str(e)}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
