from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nazwa_firmy = models.CharField(max_length=225, blank=True)
    adres = models.CharField(max_length=255, blank=True)
    kod_pocztowy = models.CharField(max_length=20, blank=True)
    miasto = models.CharField(max_length=120, blank=True)
    NIP = models.CharField(max_length=20, blank=True)
    telefon = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return 'Profil użytkownika {}.'.format(self.user.username)



