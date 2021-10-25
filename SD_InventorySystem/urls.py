from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='SD_InventorySystem'),
    path('mainpage/', views.mainpage, name='SD_InventorySystem-mainpage'),
    path('delivery/', views.delivery, name='SD_InventorySystem-delivery'),
    path('withdraw/', views.withdraw, name='SD_InventorySystem-withdraw'),
    path('status/', views.status, name='SD_InventorySystem-status'),
]