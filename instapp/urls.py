from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('',views.login_user, name='login'),
    path('register/',views.register, name='register'),
    path('logout/',auth_view.LogoutView.as_view(template_name='insta/logout.html'), name="logout"),
    path('home/',views.home, name='home'),
    path('profile/<int:user_id>',views.profile, name='profile'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns+= 