from django.db import models


class ApartmentSaleHanoi(models.Model):
    # stt = models.TextField(primary_key=True)
    title = models.TextField(primary_key=True, max_length=100)
    address = models.TextField(blank=True, null=True)
    direction = models.TextField(blank=True, null=True)
    commune = models.TextField(blank=True, null=True)
    commune_encoded = models.BigIntegerField(blank=True, null=True)
    district = models.TextField(blank=True, null=True)
    district_encoded = models.BigIntegerField(blank=True, null=True)
    province = models.TextField(blank=True, null=True)
    province_encoded = models.BigIntegerField(blank=True, null=True)
    paper = models.BigIntegerField(blank=True, null=True)
    price_by_area = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        managed = False
        db_table = 'apartment_sale_hanoi'
    
        
# class ApartmentSaleHanoi(models.Model):
#     title = models.CharField(max_length=1000, unique=False)
#     address = models.CharField(max_length=100)
#     commune = models.CharField(max_length=50)
#     commune_encoded = models.IntegerField()
#     district = models.CharField(max_length=50)
#     district_encoded = models.IntegerField()
#     province = models.CharField(max_length=50)
#     province_encoded = models.IntegerField()
#     paper = models.IntegerField()
#     price_by_area = models.BigIntegerField()
#     latitude = models.FloatField()
#     longitude = models.FloatField()
    
#     # drug_img = models.ImageField(upload_to='images/')
#     def __str__(self):
#         return self.title