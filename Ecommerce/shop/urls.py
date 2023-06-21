from django.contrib import admin
from django.urls import path
from shop import views
app_name="shop"
urlpatterns = [

    path('',views.allProdCat,name="allprodcat"),
    path('allproducts/<slug:cslug>',views.allproducts,name="allproducts"),
    path('prodetail/<slug:pslug>',views.prodetail,name="prodetail"),
    path('register/',views.register,name="register"),
    path('login/',views.user_login,name="user_login"),
    path('logout/',views.user_logout,name="user_logout"),

]