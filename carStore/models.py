from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
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