from django.shortcuts import render
from rest_framework import viewsets
from manager_api.serializers import KaryawanSerializer
from manager_api.models import Karyawan
# Create your views here.
class KaryawanViewSet(viewsets.ModelViewSet):
   queryset = Karyawan.objects.all()
   serializer_class = KaryawanSerializer