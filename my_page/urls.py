"""
URL configuration for my_page project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from horoscope.views import index

admin.AdminSite.site_header = "Моя админка"
admin.AdminSite.index_title = "Super админка"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("horoscope/", include('horoscope.urls')),
    path('todo_week/', include('week_days.urls')),
    path('actor_wiki/', include('actor_wiki.urls')),
    path('', index, name='home-page'),
    path('calculate_geometry/', include('geometry.urls')),
    path('guiness_records/', include('guinness_records.urls')),
    path('test_app/', include('app_for_tests.urls')),
    path('movie/', include('movie_app.urls')),
    path('feedback/', include('feedback.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
]
