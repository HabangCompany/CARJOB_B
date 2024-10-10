from django.db import models
from django.contrib.auth.models import AbstractUser
from carStore.models import CarStore



#유저 주소
class UserAddress(models.Model):
    postal_code = models.CharField(max_length=6, blank=False)  # 우편번호
    street_address = models.CharField(max_length=30, blank=False)  # 도로명 주소
    jibun_address = models.CharField(max_length=30, blank=True, null=True)  # 지번 주소
    detail_address = models.CharField(max_length=30, blank=False)  # 상세 주소

    def __str__(self):
        return f"{self.street_address}, {self.postal_code}"
    
    
class User(AbstractUser):
    email =models.EmailField(unique=True) # 유일한 이메일 입력
    name = models.CharField(max_length=5, blank=False)
    phoneNumber = models.CharField(max_length=15, blank=False)
    # User와 UserAddress 1:1 관계 설정
    address = models.OneToOneField(UserAddress, on_delete=models.CASCADE, null=True, blank=True)
    carModel = models.CharField(max_length=10)
    is_Store = models.BooleanField(default=False)
    store= models.ForeignKey(CarStore, on_delete=models.CASCADE,null=True, blank=True)
    first_name = None
    last_name = None

    def __str__(self):
        return self.email