"""
URL configuration for News_Reader project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from CoreNewsNexus import views
from CoreNewsNexus import views
from django.contrib import admin

urlpatterns = [
    path('admin/',admin.site.urls , name='admin') ,
    path('', views.home, name='home'),
    path('RegisterAs',views.RegisterAs,name="RegisterAs"),
    path('About',views.About,name="About"),
    path('Contact',views.Contact,name="Contact"),
    path('Login',views.Login,name="Login"),
    path('feed_post',views.feed_post,name="feed_post"),
    path('Save_Item/<str:feed_id>/',views.Save_Item,name="Save_Item"),
    path('Saved_Items_List',views.Saved_Items_List,name="Saved_Items_List"),
    path('Already_Saved',views.Already_Saved,name="Already_Saved"),
    path('User_Register',views.User_Register,name="User_Register"),
    path('Login_Submmission',views.Login_Submmission,name="Login_Submmission"),
    path('Admin_Register',views.Admin_Register,name="Admin_Register"),
    path('admin_register_submit',views.admin_register_submit,name="admin_register_submit"),
    path('user_register_submit',views.user_register_submit,name="user_register_submit"),
    
    






]

