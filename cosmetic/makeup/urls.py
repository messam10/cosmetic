from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:pro_id>', views.productDetail, name="product-detail"),
    path('add_Product/', views.add_Product, name='add Product'),
    # path(),
]