from django.contrib import admin
from django.db import models
from django_json_widget.widgets import JSONEditorWidget

from import_export.admin import ImportExportModelAdmin
from .models import ApartmentSaleHanoi
from .djongo_models import ApartmentSaleHanoiDjongo


class ApartmentSaleHanoiAdminConfig(ImportExportModelAdmin):
    model = ApartmentSaleHanoi
    search_fields = ('title', 'address')
    # list_filter = ('email', 'is_active', 'is_staff', 'created_at', 'updated_at')
    ordering = ('-price_by_area',)
    list_display = ( 'title', 'address', 'direction', 'latitude', 'longitude', 'price_by_area')
    

class ApartmentSaleHanoiDjongoAdminConfig(ImportExportModelAdmin):
    model = ApartmentSaleHanoiDjongo
    search_fields = ('title', 'address')
    # list_filter = ('email', 'is_active', 'is_staff', 'created_at', 'updated_at')
    ordering = ('-price_by_area',)
    list_display = ( 'title', 'address', 'direction', 'latitude', 'longitude', 'price_by_area')
    # formfield_overrides = {
    #     models.JSONField: {'widget': JSONEditorWidget},
    # }

    



admin.site.register(ApartmentSaleHanoi, ApartmentSaleHanoiAdminConfig)
admin.site.register(ApartmentSaleHanoiDjongo, ApartmentSaleHanoiAdminConfig)
# multi_models = [models.ApartmentSaleHanoi, djongo_models.ApartmentSaleHanoi]  # iterable list
# admin.site.register(multi_models)
