"""
URL configuration for educational_website project.

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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('table/', views.tableview, name='table'),
    path('', views.homeview, name="home"),
    path('VIIIclass/', views.VIIIclassview, name="VIIIclass"),
    path('IXclass/', views.IXclassview, name="IXclass"),
    path('Xclass/', views.Xclassview, name="Xclass"),
    path('photos/', views.photosview, name="photos"),
    path('videos/', views.videosview, name="videos"),
    path('parent_reg/', views.parent_regview, name='parent_reg'),
    path('latest_news/', views.latest_newsview),
    path('contact_us/', views.contactview, name="contact_us"),
    path('data/',views.Dataview),
]
