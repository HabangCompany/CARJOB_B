from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

#가게 위치
class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

    def clean(self):
        if not -90 <= self.latitude <= 90:
            raise ValidationError("위도는 -90에서 90 사이의 값이어야 합니다.")
        if not -180 <= self.longitude <= 180:
            raise ValidationError("경도는 -180에서 180 사이의 값이어야 합니다.")

    def __str__(self):
        return f"Latitude: {self.latitude}, Longitude: {self.longitude}"
    
#가게 시공기술들
class  sigongSkill(models.Model):
    #세차블박어쩌구저쩌구
    pass

#자동차 샵
class CarStore(models.Model):
    storeName = models.CharField(max_length=20, blank=False, verbose_name="가게이름") #가게이름
    sigongSkill = models.OneToOneField(sigongSkill, on_delete=models.CASCADE, blank=True,  verbose_name="시공기술") #시공기술
    storeLocation =  models.OneToOneField(Location, verbose_name="가게위치", on_delete=models.CASCADE) #가게위치


#유저 주소
class UserAddress(models.Model):
    postal_code = models.CharField(max_length=10, blank=False)  # 우편번호
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