from django.contrib import admin
from django.urls import path
from zenblogs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('category/', views.category, name='category'),
    path('single-post/', views.single_post, name='single-post'),
    path('starter-page/', views.starter_page, name='starter-page'),




]