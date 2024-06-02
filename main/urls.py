from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('',views.home),
    #path('register',views.register,name='register'),
    path('update',views.update,name='update'),
    path('delete',views.delete,name='delete'),
    path('upload',views.upload,name='upload'),
    #path('result',views.result,name='result'),
   # path('remove/<int:id>',views.remove,name='remove'),
]