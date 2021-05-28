from django.db import models


from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.

class Sector(models.Model):
    sector_name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Sektor Tabel'

    def __str__(self):
        return self.sector_name

class LogoImage(models.Model):
    image_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='logo/')

    class Meta:
        verbose_name_plural = 'Logo'

    def __str__(self):
        return self.image_name

class StartUp(models.Model):
    startup = models.CharField(max_length= 200)
    website = models.CharField(max_length=200, default='-')
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    deskripsi = models.TextField(default='-')
    image = models.ManyToManyField(LogoImage)
    profit = models.CharField(max_length=20)
    
    class Meta:
        verbose_name_plural='Startup'

    def __str__(self):
        return self.startup

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)