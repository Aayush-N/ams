from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
	url(r'^$', views.MainView.as_view(), name='initial'),
   	url(r'^entry/', views.AttendanceView.as_view(), name='main'),
]