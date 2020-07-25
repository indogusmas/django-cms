from django.urls import path
from .  import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home, name="home"),
    path('user/',views.userPage,name ="user-page"),
    path('account/',views.accountsSettings,name = 'account'),
    path('products/',views.products, name="products"),
    path('login',views.loginPage, name="login"),
    path('logout', views.logoutUser,name="logout"),
    path('register',views.registerPage,name="register"),
    path('customers/<str:pk_test>',views.customer,name="customer"),
    path('create_order/<str:pk>',views.createOrder, name='create_order'),
    path('update_order/<str:pk>/',views.updateOrder, name='update_order'),
    path('delete_order/<str:pk>/',views.deleteOrder, name='delete_order')
]