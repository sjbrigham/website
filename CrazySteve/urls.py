"""CrazySteve URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from bridgeapp.veiws import(
    blog_post_detail_page,
    blog_post_list_page
)
from .veiws import(
    home_page,
    fancy_words,
    bridges,
)

urlpatterns = [
    path('', home_page, name='home'),
    path('bridges', bridges),
    path('fancy_words/', include('bridgeapp.urls')),
    path('crazyadmin/', admin.site.urls),
]
