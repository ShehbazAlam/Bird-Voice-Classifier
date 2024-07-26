
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dev-admin/', admin.site.urls),
    path('admin/', include('app_admin.urls')),
    path('auth/', include('user.urls')),
    path('', include('bird_voice_classifier.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
