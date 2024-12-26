from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer, LoginSerializer
from .models import User

#회원가입
@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#로그인
@api_view(['POST'])
def login_user(request):
    serializer = LoginSerializer(data= request.data)

    if serializer.is_valid():
        return Response({
            'refresh': serializer.validated_data['refresh_token'],
            'access': serializer.validated_data['access_token']
        }, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#이메일 중복확인
@api_view(['POST'])
def check_email(request):
    email = request.data.get('email')  # POST 데이터에서 email 가져오기
    if not email:
        return Response({'error': '이메일이 없습니다.', 'code':'MISSING_EMAIL'}, status=status.HTTP_400_BAD_REQUEST)
    
    # 이메일 중복 확인
    if User.objects.filter(email=email).exists():
        return Response({'error': '중복된 이메일입니다.', 'code':'EMAIL_DUPLICATE'}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({'message': '사용 가능한 이메일입니다.', 'code':'EMAIL_AVAILABLE'}, status=status.HTTP_200_OK)

#닉네임 중복확인
@api_view(['POST'])
def check_nickname(request):
    nickname = request.data.get('nickname')

    if not nickname:
        return Response({'message':'닉네임이 없어요', 'code':'MISSING_NICKNAME'}, status=status.HTTP_400_BAD_REQUEST)
    
    if User.objects.filter(nickname=nickname).exists():
        return Response({'error': '중복된 닉네임입니다.', 'code':'NICKNAME_DUPLICATE'}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({'message': '사용 가능한 닉네임 입니다.', 'code':'NICKNAME_AVAILABLE'}, status=status.HTTP_200_OK)
