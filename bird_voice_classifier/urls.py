from django.urls import path
from .views import predict, signup, index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('predict', predict),
    path('signup', signup),
    path('', index),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)