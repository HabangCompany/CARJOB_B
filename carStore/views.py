from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import CarStore
from accounts.models import User
from .serializers import CarStoreSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def registerCarStore(request):

    user= request.user

    if user.store_id :
        print("가게있음")
        return Response({"message":"가게가 이미 등록 되어있어요"},status=status.HTTP_400_BAD_REQUEST)

    serializer = CarStoreSerializer(data = request.data)
    if serializer.is_valid():
        car_store = serializer.save()
        user.is_Store = True
        user.store = car_store
        user.save()

        return Response({"message": "자동차 가게가 성공적으로 설정되었습니다."}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)