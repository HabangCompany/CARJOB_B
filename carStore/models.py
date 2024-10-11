from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
#가게 위치
class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    storePostal_code = models.CharField(max_length=10, blank=False)  # 우편번호
    storeStreet_address = models.CharField(max_length=30, blank=False)  # 도로명 주소
    storeJibun_address = models.CharField(max_length=30, blank=True, null=True)  # 지번 주소
    storeDetail_address = models.CharField(max_length=30, blank=False)  # 상세 주소

    def clean(self):
        if not -90 <= self.latitude <= 90:
            raise ValidationError("위도는 -90에서 90 사이의 값이어야 합니다.")
        if not -180 <= self.longitude <= 180:
            raise ValidationError("경도는 -180에서 180 사이의 값이어야 합니다.")

    def __str__(self):
        return f"가게위치 위도: {self.latitude}, 경도: {self.longitude}"
    
#가게 시공기술들
class SigongSkill(models.Model):
    tinting = models.BooleanField(default=False, verbose_name="썬팅")  # 썬팅
    wrapping = models.BooleanField(default=False, verbose_name="랩핑")  # 랩핑
    ppf = models.BooleanField(default=False, verbose_name="PPF/차량보호필름")  # PPF/차량보호필름
    carwash = models.BooleanField(default=False, verbose_name="세차")  # 세차
    gloss = models.BooleanField(default=False, verbose_name="광택")  # 광택
    detail_carwash = models.BooleanField(default=False, verbose_name="디테일세차")  # 디테일세차
    car_repair = models.BooleanField(default=False, verbose_name="차량수리")  # 차량수리
    painting = models.BooleanField(default=False, verbose_name="판금/도장")  # 판금/도장
    autoglass = models.BooleanField(default=False, verbose_name="유리교체")  # 유리교체
    tire = models.BooleanField(default=False, verbose_name="타이어")  # 타이어
    engine_oil = models.BooleanField(default=False, verbose_name="엔진오일")  # 엔진오일
    blackbox = models.BooleanField(default=False, verbose_name="블랙박스")  # 블랙박스
    navigation = models.BooleanField(default=False, verbose_name="네비게이션")  # 네비게이션
    led = models.BooleanField(default=False, verbose_name="LED")  # LED
    rear_camera = models.BooleanField(default=False, verbose_name="후방카메라")  # 후방카메라
    rear_sensor = models.BooleanField(default=False, verbose_name="후방감지기")  # 후방감지기
    light_restoration = models.BooleanField(default=False, verbose_name="라이트복원")  # 라이트복원
    rent_car = models.BooleanField(default=False, verbose_name="렌트카")  # 렌트카

    def __str__(self):
        return "시공 기술 설정"



#자동차 샵
class CarStore(models.Model):
    storeName = models.CharField(max_length=20, blank=False, verbose_name="가게이름") #가게이름
    sigongSkill = models.OneToOneField(SigongSkill, on_delete=models.CASCADE, blank=True,  verbose_name="시공기술") #시공기술
    storeLocation =  models.OneToOneField(Location, verbose_name="가게위치", on_delete=models.CASCADE) #가게위치
    thumbnail = models.ImageField(upload_to='car_store_thumbnail', blank=False)

    def __str__(self):
        return self.storeName

#가게사진
class StorePhoto(models.Model):
    car_store = models.ForeignKey("CarStore", on_delete=models.CASCADE, related_name='photos' )
    photo = models.ImageField(upload_to='store_photo', verbose_name="가게사진")