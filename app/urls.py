from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index,name="index"),
    path('home/',views.home,name="home"),
    path('calculator',views.calculator,name="calculator"),
    path('delete/<int:id>/',views.delete_consume,name="delete"),
    # path('register/', views.register, name='register'),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout_view, name='logout'),
    
]