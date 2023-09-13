from film.serializers import *
from unittest import TestCase

class TestAktyorSerializer(TestCase):
    def test_aktyor(self):
        aktyor = {
            "id":3,
            "ism":"Kamol Qahhorov",
            "davlat":"O'zbekiston",
            "tugilgan_yil":"1980-01-10",
            "jins":"Erkak"
        }
        serializer = AktyorSerializer(data=aktyor)
        assert serializer.is_valid() == True
        # self.assertTrue(serializer.is_valid == True) # 2-usul

        assert serializer.validated_data is not None
        malumot = serializer.validated_data
        assert malumot["ism"] == "Kamol Qahhorov"
        assert malumot["davlat"] == "O'zbekiston"
        assert malumot["jins"] == "Erkak"
        assert True == True

    def test_invalid_ism(self):
        aktyor = {
            "id": 3,
            "ism": "Ka",
            "davlat": "O'zbekiston",
            "tugilgan_yil": "1980-01-10",
            "jins": "Erkak"
        }
        serializer = AktyorSerializer(data=aktyor)
        assert serializer.is_valid() == False
        assert serializer.errors["ism"][0] == "Ism bunaqa kalta bo'lishi mumkin emas"
    def test_invalid_jins(self):
        aktyor = {
            "id": 3,
            "ism": "Kamol",
            "davlat": "O'zbekiston",
            "tugilgan_yil": "1980-01-10",
            "jins": "ERKAK"
        }
        serializer = AktyorSerializer(data=aktyor)
        assert serializer.is_valid() == False
        assert serializer.errors["jins"][0] == "Erkak yoki Ayol so'zidan biri bo'lishi kerak"

class TestKinoSerializer(TestCase):
    def test_kino(self):
        kino = {
            "id":2,
            "nom": "Sotqin",
            "janr": "Action",
            "yil": "2018-05-22",
            "aktyorlar":[1,2]

        }
        serializer = KinoCreateSerializer(data=kino)
        assert serializer.is_valid() == True

        assert serializer.validated_data['nom'] == "Sotqin"


