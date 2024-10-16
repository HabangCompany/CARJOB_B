from rest_framework import serializers
from .models import CarStore, Location, SigongSkill

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class SigongSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = SigongSkill
        fields = '__all__'

class CarStoreSerializer(serializers.ModelSerializer):
    storeLocation = LocationSerializer()  # Nested serializer
    sigongSkill = SigongSkillSerializer()  # Nested serializer
    thumbnail = serializers.ImageField(required=False)

    class Meta:
        model = CarStore
        fields = ['storeName', 'storeLocation', 'sigongSkill', 'thumbnail', 'business_hours', 'holidays', 'store_phone']

    def create(self, validated_data):
        # 먼저 Location 및 SigongSkill 데이터를 가져옴
        location_data = validated_data.pop('storeLocation')
        sigong_skill_data = validated_data.pop('sigongSkill')

        # 중첩된 데이터를 이용해 Location 및 SigongSkill 객체 생성
        location = Location.objects.create(**location_data)
        sigong_skill = SigongSkill.objects.create(**sigong_skill_data)

        # CarStore 객체를 생성하고 위에서 만든 객체를 연결
        car_store = CarStore.objects.create(storeLocation=location, sigongSkill=sigong_skill, **validated_data)

        return car_store