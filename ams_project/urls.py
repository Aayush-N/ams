"""ams_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views.generic import RedirectView

urlpatterns = [
    # JET page
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    # Admin Page
    url(r'^dashboard/', include(admin.site.urls)),
    # Login and logout URLs
    url(r"^accounts/", include("registration.backends.hmac.urls")),
    # Attendance URLs
    url(r"^attendance/", include("main.urls")),
    # Dashboard URLs
    # url(r"^dashboard/", include("dashboard.urls")),
    # Redirecting / to /attendance/
    url(r"^$", RedirectView.as_view(url="/attendance/")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
