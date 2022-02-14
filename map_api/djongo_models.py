from email.policy import default
from unittest.util import _MAX_LENGTH
# import uuid


from djongo import models



class ApartmentSaleHanoiDjongo(models.Model):
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
        db_table = 'apartment_sale_hanoi'
        abstract = False # meaning all in one table
        