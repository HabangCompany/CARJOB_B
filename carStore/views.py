from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CarStore
from accounts.models import User
from .serializers import CarStoreSerializer


@api_view(['POST'])
def registerCarStore(request):
    user= request.user
    serializer = CarStoreSerializer(data = request.data)
    if serializer.is_valid():
        car_store = serializer.save()
        user.is_Store = True
        user.store = car_store
        user.save()

        return Response({"message": "자동차 가게가 성공적으로 설정되었습니다."}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)