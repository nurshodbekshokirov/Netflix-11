
from django.contrib import admin
from django.urls import path,include
from film.views import *
from rest_framework.authtoken.views import  obtain_auth_token
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Netflix API",
      default_version='v1',
      description="O'quv maqsadlarida foydalanish uchun Netflix API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact("Nurshodbek Shokirov,<nurshodbekshokirov@gmail.com>"),

   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
router = DefaultRouter()
router.register("izohs", IzohModelViewset)
router.register("kinolar", KinoViewSet)
router.register("aktyorlar", AktyorVIEWsET)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', HelloAPI.as_view()),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('docs2/', schema_view.with_ui('redoc', cache_timeout=0)),
    # path('aktyorlar/', AktyorlarAPIView.as_view()),
    path('tariflar/', TariflarAPIView.as_view()),
    path('tarif/<int:pk>/', TarifAPIView.as_view()),
    # path('aktyor/<int:pk>/', AktyorDetailAPIView.as_view()),
    # path('kino/<int:pk>/', KinoDetailApiView.as_view()),
    # path('kinolar/', KinolarApiView.as_view()),
    path("", include(router.urls)),
    path('get_token/', obtain_auth_token)
]
