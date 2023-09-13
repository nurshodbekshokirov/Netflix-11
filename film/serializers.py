from rest_framework.exceptions import APIException

from .models import *
from rest_framework import serializers

class AktyorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    ism = serializers.CharField(max_length=30)
    tugilgan_yil = serializers.DateField()
    davlat = serializers.CharField(max_length=30, allow_blank=True)
    jins = serializers.CharField(max_length=30)

    def validate_jins(self, qiymat: str):
        if qiymat!='Erkak' and qiymat!='Ayol':
            raise serializers.ValidationError("Erkak yoki Ayol so'zidan biri bo'lishi kerak")
        return qiymat
    def validate_ism(self, qiymat:str):
        if len(qiymat)<3:
            raise serializers.ValidationError("Ism bunaqa kalta bo'lishi mumkin emas")
        return qiymat

    def create(self, validated_data):
        return Aktyor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.ism = validated_data.get('ism', instance.ism)
        instance.tugilgan_yil = validated_data.get('tugilgan_yil', instance.tugilgan_yil)
        instance.davlat = validated_data.get('davlat', instance.davlat)
        instance.jins = validated_data.get('jins', instance.jins)
        instance.save()
        return instance


class TarifSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nom = serializers.CharField(max_length=30)
    muddat = serializers.CharField(max_length=30)
    narx = serializers.IntegerField()

class KinoSerializer(serializers.ModelSerializer):
    aktyorlar = AktyorSerializer(many=True)
    class Meta:
        model = Kino
        fields = '__all__'

class KinoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kino
        fields = '__all__'
class IzohSerializer(serializers.ModelSerializer):
    class Meta:
        model = Izoh
        fields = "__all__"