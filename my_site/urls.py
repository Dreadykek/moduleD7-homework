from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('p_library.urls')),
    path('account/', include('common.urls')),
    path('accounts/', include('allauth.urls')),
]
