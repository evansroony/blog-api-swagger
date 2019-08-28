from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),  # new
    path('api/v1/', include('posts.urls')),  # new
    path('admin/', admin.site.urls),
]
