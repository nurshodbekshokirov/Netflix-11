from film.models import *
from unittest import TestCase
from rest_framework.test import APIClient

class TestAktyorAPIViews(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()


    def test_all_actors_view(self):
        natija = self.client.get('/aktyorlar/')
        assert natija.status_code == 200
        assert len(natija.data) == Aktyor.objects.count()
        if len(natija.data) != 0:
            assert natija.data[0]['ism'] == Aktyor.objects.first().ism
            assert natija.data[0]['davlat'] == Aktyor.objects.first().davlat
            assert natija.data[0]['jins'] == Aktyor.objects.first().jins
    def test_actor_view(self):
        natija = self.client.get('/aktyorlar/1/')
        assert natija.status_code == 200

        assert natija.data['ism'] == Aktyor.objects.get(id=1).ism
        assert natija.data['davlat'] == Aktyor.objects.get(id=1).davlat
    def test_aktyor_invalid_jins(self):
        aktyor = {
            "ism":"Emma Watson",
            "jins":"ayol",
            "davlat":"Angliya",
            "tugilgan_yil": "1995-07-29"
        }
        natija = self.client.post('/aktyorlar/', data=aktyor)
        assert natija.status_code == 400
        assert natija.data['jins'][0] == "Erkak yoki Ayol so'zidan biri bo'lishi kerak"

    def test_aktyor_invalid_ism(self):
        aktyor = {
            "ism":"Em",
            "jins":"Ayol",
            "davlat":"Angliya",
            "tugilgan_yil": "1995-07-29"
        }
        natija = self.client.post('/aktyorlar/', data=aktyor)
        assert natija.status_code == 400
        assert natija.data['ism'][0] == "Ism bunaqa kalta bo'lishi mumkin emas"

    # def test_aktyor_invalid_qoshish(self):
    #     aktyor = {
    #         "ism":"Emma Watson",
    #         "jins":"Ayol",
    #         "davlat":"Angliya",
    #         "tugilgan_yil": "1995-07-29"
    #     }
    #     natija = self.client.post('/aktyorlar/', data=aktyor)
    #     assert natija.status_code == 201
    #     assert natija.data['id'] is not None
    #     assert natija.data['ism'] == Aktyor.objects.last().ism
    #     assert natija.data['davlat'] == Aktyor.objects.last().davlat
    #     assert natija.data['jins'] == Aktyor.objects.last().jins


    def test_aktyor_ozgartirish(self):
        aktyor = {


            "ism": "Densel Washington",
            "tugilgan_yil": "1995-07-29",
            "davlat": "Aqsh",
            "jins": "Erkak"
        }
        natija = self.client.put('/aktyorlar/6/', data=aktyor)
        # print(natija.status_code)
        assert natija.status_code == 200
        assert natija.data['ism'] == "Densel Washington"
        assert natija.data['davlat'] == "Aqsh"




