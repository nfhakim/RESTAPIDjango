from django.db import models

# Create your models here.
class Karyawan(models.Model):
    nama = models.CharField(max_length=100)
    id_karyawan = models.CharField(max_length=100)
    posisi = models.CharField(max_length=100)