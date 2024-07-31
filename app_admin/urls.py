from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from app_admin.views import dashboard, user_list, user_detail, predications_list, prediction_detail

urlpatterns = [
    path('dashboard', dashboard, name="dashboard"),
    path('user-list', user_list, name='user_list'),
    path('user-details', user_detail, name='user_detail'),
    path('predictions-list', predications_list, name="prediction_list"),
    path('prediction-detail', prediction_detail, name='prediction_detail')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)