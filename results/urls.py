from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('insert/imageuploading', views.upload_image,name='image_loading'),
    path('insert/',views.insert,name='display'),
    path('database/',views.database,name='database'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('result/',views.result,name='result'),
    path('percentage/<str:name>',views.percentage,name='percentage'),
    path('res/', views.res,name='res')
    ]
