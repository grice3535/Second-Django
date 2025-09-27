"""
URL configuration for classproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from blog import views as blog_views
from carapp import views as car_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_views.index, name="index"),
    path('why/', blog_views.why, name="why"),
    path('post_list/', blog_views.show_post, name="post"),
    path('car_list/', car_views.car_list, name="car"),
]

