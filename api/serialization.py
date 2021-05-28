from rest_framework import serializers

from .models import *

class SectorSerialization(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'

class LogoImageSerialization(serializers.ModelSerializer):
    class Meta:
        model = LogoImage
        exclude=['id']

class StartUpSerialization(serializers.ModelSerializer):
    image = LogoImageSerialization(read_only=True, many=True)
    class Meta:
        model = StartUp
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['sector'] = SectorSerialization(read_only=True)
        return super(StartUpSerialization, self).to_representation(instance)