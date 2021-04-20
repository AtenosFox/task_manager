from django.urls import path
from django.urls import include
from . import views
from .views import (
    LoginView
)

urlpatterns = [
    path('', views.index, name='index'),
    path('about-us', views.about, name='about'),
    path('create', views.create, name='create'),
    # path('accounts/', include('allauth.urls')),
    path('delete_task/<int:id>/', views.delete_task),
    path('login', LoginView.as_view(), name='login')

]
