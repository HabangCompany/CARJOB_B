from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only= True) #비밀번호는 쓰기전용임

    class Meta:
        model = User
        fields = ('email', 'name', 'phoneNumber', 'password', 'carModel')

    def create(self, validated_data):
        # 새로운 유저를 생성할 때, 비밀번호를 해시화하여 저장
        user = User(
            email=validated_data['email'],
            name=validated_data['name'],
            phoneNumber=validated_data['phoneNumber'],
            carModel=validated_data['carModel']
        )
        user.set_password(validated_data['password'])  # 비밀번호 해시화
        user.save()
        return user