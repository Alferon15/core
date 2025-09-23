from django.contrib import admin
from django.urls import path
from django.urls.conf import include

app_name = 'core'

urlpatterns = [
    path('', include('base_app.urls'), name='home'),
    path('storage/', include('storage.urls')),
    path('users/', include('users.urls')),
    
    path('admin/', admin.site.urls),
]
