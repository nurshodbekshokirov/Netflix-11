
from django.contrib import admin
from django.urls import path,include
from film.views import *
from rest_framework.authtoken.views import  obtain_auth_token
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("izohs", IzohModelViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', HelloAPI.as_view()),
    path('aktyorlar/', AktyorlarAPIView.as_view()),
    path('tariflar/', TariflarAPIView.as_view()),
    path('tarif/<int:pk>/', TarifAPIView.as_view()),
    path('aktyor/<int:pk>/', AktyorDetailAPIView.as_view()),
    path('kino/<int:pk>/', KinoDetailApiView.as_view()),
    path('kinolar/', KinolarApiView.as_view()),
    path("", include(router.urls)),
    path('get_token/', obtain_auth_token)
]
