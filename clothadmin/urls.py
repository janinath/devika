from django.urls import path
from.import views
app_name='clothadmin'
urlpatterns=[
    path('login/',views.adminlogin,name='adminlogin'),
    path('viewproducts/',views.viewproducts,name='viewpdt'),
    path('addproducts/',views.addproducts,name='addpdt'),
    path('p_delete/<int:pid>',views.deleteproduct,name='p_delete'),
    path('sdashboard/',views.sdashboard,name='sdashboard'),
    path('addstaffs/',views.addstaffs,name='addstaffs'),
    path('p_update/<int:pid>',views.updateproduct,name='p_update'),
    path('update/',views.update,name='update'),
    path('viewstaffs/',views.viewstaffs,name='viewstaffs'),
    path('s_delete/<int:sid>',views.deletestaff,name='s_delete')


   


]