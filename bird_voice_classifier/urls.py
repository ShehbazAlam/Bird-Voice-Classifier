from django.urls import path
from .views import login, signup
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login', login),
    path('signup', signup),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)