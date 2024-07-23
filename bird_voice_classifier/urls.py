from django.urls import path
from .views import index, result
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name="home"),
    path('result', result, name="result"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)