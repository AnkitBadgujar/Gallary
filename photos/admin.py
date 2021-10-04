from django.contrib import admin
from . models import Photo,Category

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id','category','description','image']

