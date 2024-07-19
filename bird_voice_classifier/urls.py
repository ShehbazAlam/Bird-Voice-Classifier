from django.urls import path
from .views import login, signup, index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('predict', login),
    path('signup', signup),
    path('', index),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)