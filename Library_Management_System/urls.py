
from django.contrib import admin
from django.urls import path,include,re_path
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth.views import LogoutView
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
       path('', include('api.urls')),
       path('auth/',obtain_auth_token),
       re_path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
]

