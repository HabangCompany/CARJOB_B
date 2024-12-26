from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from .models import User, UserAddress

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer()  # 중첩된 AddressSerializer 사용
    password = serializers.CharField(write_only=True) # 비밀번호는 쓰기전용 그래야 리턴이 안됨

    class Meta:
        model = User
        fields = ('email', 'nickname', 'phone_number', 'password', 'address')

    #회원가입
    def create(self, validated_data):
        # 중첩된 address 데이터 추출 및 저장
        address_data = validated_data.pop('address')
        address = UserAddress.objects.create(**address_data)

        # User 생성
        user = User(
            username = validated_data['email'],
            email=validated_data['email'],
            nickname=validated_data['nickname'],
            phone_number=validated_data['phone_number'],
            address=address
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