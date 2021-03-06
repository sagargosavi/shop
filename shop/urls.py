"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'shop_app.views.index', name='index'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^login1/$','shop_app.register.register_page',name='register'),
    url(r'^register/$','shop_app.register.register_page',name='register'),
    url(r'^register/success/$','shop_app.register.register_success'),
    url(r'logout/$','shop_app.register.logout',name='logout')
]
