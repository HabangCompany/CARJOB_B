from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only= True) #비밀번호는 쓰기전용임

    class Meta:
        model = User
        fields = ('email', 'name', 'phone_number', 'password', 'car_model')

    def create(self, validated_data):
        # 새로운 유저를 생성할 때, 비밀번호를 해시화하여 저장
        user = User(
            email=validated_data['email'],
            name=validated_data['name'],
            phone_number=validated_data['phone_number'],
            car_model=validated_data['car_model'],
            username=validated_data['email']
        )
        user.set_password(validated_data['password'])  # 비밀번호 해시화
        user.save()
        return user
    
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField() # 아이디
    password = serializers.CharField(write_only= True) #비밀번호 쓰기전용 (응답으로 비번을전달하지않음)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(username=email, password=password)

            if user:
                refresh = RefreshToken.for_user(user)
                data['refresh_token'] = str(refresh)
                data['access_token'] = str(refresh.access_token)
            else:
                raise serializers.ValidationError('잘못된 이메일 또는 비밀번호입니다')
        
        else:
            raise serializers.ValidationError("아이디와 비밀번호가 틀렸습니다.")
        
        return data