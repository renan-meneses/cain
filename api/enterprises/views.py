from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import EnterprisesModel
from .serializers import EnterpriseSerializer


class ListEnterprise(generics.GenericAPIView):
    queryset = EnterprisesModel.objects.all()
    serializer_class = EnterpriseSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serialize = EnterpriseSerializer(queryset, many=True)
            return Response(serialize.data, status=status.HTTP_200_OK)
        except Exception as e:
            response = {"erro": str(e)}
            return Response(response, status=status.HTTP_404_NOT_FOUND)

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
            return Response(response, status=status.HTTP_404_NOT_FOUND)


class CreateEnterprise(generics.CreateAPIView):
    queryset = EnterprisesModel.objects.all()
    serializer_class = EnterpriseSerializer
    permission_classes = (permissions.IsAuthenticated,)
