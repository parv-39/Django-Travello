from django.urls import path,include
from .import views

urlpatterns = [

    path('', views.index, name='index'),
    path('about/', views.about, name='about'), 
    path('contact/', views.contactus, name='contactus'),
    path('news/', views.news, name='news'),
    path('destination/<int:id>/', views.destination_detail, name='destination_detail'),
    path('destination/<int:id>/book/', views.book_destination, name='book_destination'),
]
