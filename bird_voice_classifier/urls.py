from django.urls import path
from .views import index, result, feedback
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name="home"),
    path('result', result, name="result"),
    path('feedback', feedback, name="feedback"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)