from django.http import JsonResponse
from rest_framework import status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import *

from .models import *
from .serializers import *

from rest_framework.views import APIView


class HelloAPI(APIView):
    def get(self, request):
        content = {
            'xabar': "Salom, Dunyo! "
        }
        return Response(content)
    def post(self,request):
        data = request.data
        content = {
            'xabar': "Post so'rov qabul qilindi",
            "ma'lumot": data
        }
        return Response(content)

# class AktyorlarAPIView(APIView):
#     def get(self,request):
#         aktyorlar = Aktyor.objects.all()
#         serializer = AktyorSerializer(aktyorlar, many=True)
#         return Response(serializer.data)
#     def post(self,request):
#
#         serializer = AktyorSerializer(data=request.data)
#         if serializer.is_valid():
#             Aktyor.objects.create(
#                 ism = serializer.validated_data.get('ism'),
#                 davlat = serializer.validated_data.get('davlat'),
#                 jins = serializer.validated_data.get('jins'),
#                 tugilgan_yil = serializer.validated_data.get('tugilgan_yil')
#             )
#             content = {
#                 "success": "True",
#                 "ma'lumot":serializer.data
#             }
#             return Response(content)
#         return Response({"success":"False", "xatolik":serializer.errors})
class AktyorVIEWsET(ModelViewSet):
    queryset = Aktyor.objects.all()
    serializer_class = AktyorSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['ism']
    ordering_fields = ['tugilgan_yil']


# class AktyorDetailAPIView(APIView):
#     def get(self,request, pk):
#         aktyor = Aktyor.objects.get(id=pk)
#         serializer = AktyorSerializer(aktyor)
#         return Response(serializer.data)
#     def put(self,request, pk):
#         aktyor = Aktyor.objects.get(id=pk)
#         yangi = request.data
#         serializer = AktyorSerializer(aktyor, yangi)
#         if serializer.is_valid():
#             aktyor.ism = serializer.validated_data.get('ism')
#             aktyor.davlat = serializer.validated_data.get('davlat')
#             aktyor.jins = serializer.validated_data.get('jins')
#             aktyor.tugilgan_yil = serializer.validated_data.get('tugilgan_yil')
#             aktyor.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#     def delete(self,request,pk):
#         aktyor = Aktyor.objects.filter(id=pk).delete()
#         if aktyor[0]==0:
#             return Response({"xabar":"Bunaqa aktyor yo'q!"})
#
#
#         return Response({"xabar": "Aktyor o'chirildi"})
class TariflarAPIView(APIView):
    def get(self,request):
        tarif = Tarif.objects.all()
        serializer = TarifSerializer(tarif, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TarifSerializer(data=request.data)
        if serializer.is_valid():
            Tarif.objects.create(
                nom = serializer.validated_data.get('nom'),
                muddat = serializer.validated_data.get('muddat'),
                narx = serializer.validated_data.get('narx')
            )
            content = {
                "xabar":"True",
                "ma'lumot":serializer.data
            }
            return Response(content)
        return Response({"xabar":"False","ma'lumot":serializer.errors})
class TarifAPIView(APIView):
    def delete(self,request,pk):
        tarif = Tarif.objects.filter(id=pk).delete()
        if tarif[0]==0:
            return Response({"xabar":"Bunaqa tarif yo'q"})
        return Response({"xabar":"Tarif o'chirildi"})
    def put(self,request,pk):
        tarif = Tarif.objects.get(id=pk)
        yangi = request.data
        serializer = TarifSerializer(tarif,yangi)
        if serializer.is_valid():
            tarif.nom = serializer.validated_data.get('nom')
            tarif.muddat = serializer.validated_data.get('muddat')
            tarif.narx = serializer.validated_data.get('narx')
            tarif.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self,request,pk):
        tarif = Tarif.objects.get(id=pk)
        serializer = TarifSerializer(tarif)
        return Response(serializer.data)
#
# class KinolarApiView(APIView):
#     def get(self, request):
#         kinolar = Kino.objects.all()
#         serializer = KinoSerializer(kinolar, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = KinoCreateSerializer(data=request.data)
#         if serializer.is_valid():
#
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class KinoDetailApiView(APIView):
#     def get(self,request, pk):
#         kino = Kino.objects.get(id=pk)
#         serializer = KinoSerializer(kino)
#         return Response(serializer.data)
#     def put(self,request,pk):
#         kino = Kino.objects.get(id=pk)
#         serializer = KinoCreateSerializer(kino, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

class KinoViewSet(ModelViewSet):
    queryset = Kino.objects.all()
    serializer_class = KinoSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nom']
    ordering_fields = ['yil']
    @action(detail=True, methods=["GET", "POST"])
    def aktyorlar(self, request, pk):
        if request.method == "POST":
            kino = Kino.objects.get(id=pk)
            serializer = AktyorSerializer(data=request.data)
            if serializer.is_valid():

                actor = Aktyor.objects.create(
                    ism=serializer.validated_data.get('ism'),
                    davlat=serializer.validated_data.get('davlat'),
                    jins=serializer.validated_data.get('jins'),
                    tugilgan_yil=serializer.validated_data.get('tugilgan_yil')
                )

                kino.aktyorlar.add(actor)
                kino.save()

        kino = Kino.objects.get(id=pk)
        actors = kino.aktyorlar.all()
        serializer = AktyorSerializer(actors, many=True)
        return Response(serializer.data)

class IzohModelViewset(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Izoh.objects.all()
    serializer_class = IzohSerializer
    def get_queryset(self):
        queryset = Izoh.objects.filter(user=self.request.user)
        return queryset
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user == self.request.user:
            instance.delete()
            return Response({"success":"True"}, status=status.HTTP_200_OK)
        return Response({"success":"False"}, status=status.HTTP_400_BAD_REQUEST)








# Create your views here.
