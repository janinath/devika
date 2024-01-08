from django.urls import path
from.import views
from django.contrib.auth import views as auth_views
app_name="clothapp"
urlpatterns=[
    path('login/',views.indexhome,name="login"),
    path('signin/',views.signin,name="signin"),
    path('',views.home,name='home'),
    path('contactus/',views.contactus,name='contactus'),
    path('dashboard/',views.Dashboard,name='dashboard'),
    path('forgetpassword/',views.forgetpassword,name='forgetpassword'),
    path('addtocart/',views.addtocart,name='addtocart'),
    path('dresses/',views.dresses,name='dresses'),
    path('sizechart/',views.sizechart,name='aboutus'),
    path('accessories/',views.accessories,name='accessories'),
    path('bags/',views.bags,name='bags'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart,name='add_to_cart'),
    path('payment/',views.payment,name='payment'),
    path('remove_from_cart/<int:product_id>',views.remove_from_cart,name='remove_from_cart'),
    path('logout/',views.logOut,name='logout')
    
    ]