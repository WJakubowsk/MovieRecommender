from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('search/', views.search, name='search'),
    path('recommend/', views.recommend, name='recommend'),
    path('info/', views.info, name='info'),
    path('omdb/<str:title>/', views.example, name='example'),
    path('about', views.about, name='about'),
]
