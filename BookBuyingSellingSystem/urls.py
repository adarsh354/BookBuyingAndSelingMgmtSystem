"""BookBuyingSellingSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(''          ,   views.home_view          , name='home'),
    path('home/<sem>/' , views.home_view          , name='home1'),
    path('admin/'	,	admin.site.urls           , name='admin'),
    path('profile/'  ,   views.profile_view       , name='profile'),
    path('register/',	views.register_view	      , name='register'),   
    path('signup/'	,	views.signup_view		  , name='signup'),
    path('login/'	,	views.login_view		  , name='login'),
    path('logout/'	,	views.logout_view		  , name='logout'),
    path('buying/<book>/' , views.buying_view       , name='buying'),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)


