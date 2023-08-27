from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.questions.urls')),
    path('auth/', obtain_auth_token),
]
