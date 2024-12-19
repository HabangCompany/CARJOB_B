from rest_framework import serializers
from .models import CarStore, Location, SigongSkill, StorePhoto

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class SigongSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = SigongSkill
        fields = '__all__'

class CarStoerPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorePhoto
        fields = ['photo','order']

class CarStoreSerializer(serializers.ModelSerializer):
    store_location = LocationSerializer()
    sigong_skill = SigongSkillSerializer()  
    storePhotos = CarStoerPhotoSerializer()
    thumbnail = serializers.ImageField(required=False) ##필수 항목이아님

    class Meta:
        model = CarStore
        fields = ['store_name', 'store_location', 'sigong_skill', 'thumbnail', 'business_hours', 'holidays', 'store_phone']

    def create(self, validated_data):
        # 먼저 Location 및 SigongSkill 데이터를 가져옴
        location_data = validated_data.pop('store_location')
        sigong_skill_data = validated_data.pop('sigong_skill')
        # 중첩된 데이터를 이용해 Location 및 SigongSkill 객체 생성
        location = Location.objects.create(**location_data)
        sigong_skill = SigongSkill.objects.create(**sigong_skill_data)
        # CarStore 객체를 생성하고 위에서 만든 객체를 연결
        car_store = CarStore.objects.create(store_location=location, sigong_skill=sigong_skill, **validated_data)
        return car_store
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)