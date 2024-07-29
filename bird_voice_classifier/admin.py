from django.contrib import admin
from .models import Prediction, Feedback

# Register your models here.
admin.site.register((Prediction, Feedback))