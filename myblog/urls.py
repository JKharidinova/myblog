from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weblog.urls')),
    path('weblog/', include('weblog.urls')),
]
