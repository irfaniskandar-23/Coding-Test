from django.urls import path, re_path
from inventory import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('api/inventory/', views.InventoryList.as_view()),
    path('api/inventory/<int:pk>', views.InventoryDetail.as_view()),
    path('inventory/', views.ViewInventory, name='Inventory'),
    path('inventory/<int:pk>', views.ViewInventoryDetail, name='Inventory_detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)
