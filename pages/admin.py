from django.contrib import admin
from pages.models import *

@admin.register(BreakfastModel)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    
    
@admin.register(LunchModel)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    
    
@admin.register(DinnerModel)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']