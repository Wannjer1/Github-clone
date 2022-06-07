from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('',views.login, name='login'),
    path('register/',views.register, name='register'),
    path('home/',views.home, name='home'),
    path('logout/',auth_view.LogoutView.as_view(template_name='insta/logout.html'), name="logout"),
]

# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)