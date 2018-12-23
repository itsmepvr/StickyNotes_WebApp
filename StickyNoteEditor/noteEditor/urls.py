
from django.urls import path, include
from . import views

app_name='noteEditor'

urlpatterns = [
    path('', views.index, name='index'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('register/', views.register, name='register'),
    path('add_note/', views.add_note, name='add_note'),
]
