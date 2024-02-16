from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<int:product_id>/', views.product, name='product'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    ]
