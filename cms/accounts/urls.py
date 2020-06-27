from django.urls import path
from .  import views

urlpatterns = [
    path('',views.home, name="home"),
    path('products/',views.products, name="products"),
    path('customers/<str:pk_test>',views.customer,name="customer")
]