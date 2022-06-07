from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.login, name='login'),
    path('register/',views.register, name='register'),
    path('home/',views.home, name='home'),
]

# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)