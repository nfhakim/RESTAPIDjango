# -*- coding: utf-8 -*-
"""
Created on Sun May  2 23:58:47 2021

@author: NFH
"""

from rest_framework import serializers
from manager_api.models import Karyawan

class KaryawanSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Karyawan
        fields = ('nama','id_karyawan','posisi')