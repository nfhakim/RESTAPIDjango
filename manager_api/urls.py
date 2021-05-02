# -*- coding: utf-8 -*-
"""
Created on Mon May  3 00:03:20 2021

@author: NFH
"""

from django.urls import include, path
from rest_framework import routers
from manager_api.views import KaryawanViewSet

router = routers.DefaultRouter()
router.register(r'people', KaryawanViewSet)

urlpatterns = [
   path('', include(router.urls)),
]