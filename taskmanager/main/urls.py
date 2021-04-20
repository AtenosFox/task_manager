from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about-us', views.about, name='about'),
    path('create', views.create, name='create'),
    path('register', views.register, name='register'),
    path('delete_task/<int:id>/', views.delete_task),
]
