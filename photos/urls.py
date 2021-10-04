from django.contrib import admin
from django.urls import path
from . import views
from .views import DeleteCategory, DeletePhoto
urlpatterns = [
    path('',views.gallery,name='gallery'),
    path('photo/<str:pk>',views.viewPhoto,name='photo'),
    path('add/',views.addPhoto,name='add'),
    path('delete_photo',DeletePhoto.as_view(),name='delete_photo' ),
    path('delete_category',DeleteCategory.as_view(),name='delete_category' ),
]