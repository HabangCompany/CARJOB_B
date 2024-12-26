from django.db import models
from django.contrib.auth.models import AbstractUser
from carStore.models import CarStore



#유저 주소
class UserAddress(models.Model):
    zone_code = models.CharField(max_length=10, blank=False)  # 우편번호
    street_address = models.CharField(max_length=50, blank=False)  # 도로명 주소
    jibun_address = models.CharField(max_length=50, blank=True, null=True)  # 지번 주소
    detail_address = models.CharField(max_length=50, blank=False)  # 상세 주소

    def __str__(self):
        return f"{self.street_address},{self.detail_address}, {self.zone_code}"
    
    
class User(AbstractUser):
    email =models.EmailField(unique=True) # 유일한 이메일 입력 
    nickname = models.CharField(max_length=20, blank=False)
    phone_number = models.CharField(max_length=15, blank=False)
    # User와 UserAddress 1:1 관계 설정
    address = models.OneToOneField(UserAddress, on_delete=models.CASCADE, null=True, blank=True)
    is_store = models.BooleanField(default=False)
    store= models.ForeignKey(CarStore, on_delete=models.SET_NULL,null=True, blank=True)
    first_name = None
    last_name = None

    USERNAME_FIELD = 'email' # 로그인할때 아이디를 이메일로 사용하긔
    REQUIRED_FIELDS = ['name', 'phone_number']  # 이메일 외에 필수로 입력할 필드

    def __str__(self):
        return self.email