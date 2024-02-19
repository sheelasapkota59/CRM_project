from django.urls import path
from . import views

urlpatterns = [
    path('' , views.dashboard , name ='dashboard'),
    path('login/' , views.login_user , name ='login'),
    path('logout/' , views.logout_user , name ='logout'),
    path('register/' , views.register_user , name ='register'),
    path('reset_password/' , views.reset_password , name = 'reset_password'),
    path('record/<int:pk>' , views.customer_record , name = 'customer_record'),
    path('delete/<int:pk>' , views.delete_record , name = 'delete_record'),
    path('add_record/' , views.add_record , name = 'add_record'),
    path('update_record/<int:pk>' , views.update_record , name = 'update_record'),
   
    
]
