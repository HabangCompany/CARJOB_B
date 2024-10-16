from rest_framework import serializers
from .models import CarStore, Location, SigongSkill

class CarStoreSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(required= False) #썸네일은 필수사항이 아님
    class Meta:
        model = CarStore
        fields = ['storeName','storeLocation','sigongSkill','thumbnail','business_hours','holidays','store_phone']

        def create(self, validated_data):
            return CarStore.objects.create(**validated_data)
