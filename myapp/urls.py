from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.signup,name='signup'),
    path('login',views.Login,name='login'),
    path('next',views.next,name='next'),
]