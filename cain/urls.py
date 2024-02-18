from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Cain API",
        default_version="v1",
        description="Gerenciado de colaboradores",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="renanmenesesdev@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("settings/", admin.site.urls),
    path(
        "api/docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("api/", include("api.accounts.urls")),
    path("api/", include("api.enterprises.urls")),
]
