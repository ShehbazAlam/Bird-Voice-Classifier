from django.shortcuts import render
from bird_voice_classifier.models import Prediction
from django.contrib.auth.models import User

# Create your views here.

def dashboard(request):
    pass

def user_list(request):
    users = User.objects.all()
    return render(request, 'dev-admin/user-list.html', {'list': users})

def user_detail(request):
    pass

def predications_list(request):
    predictions = Prediction.objects.all()
    return render(request, 'dev-admin/predictions.html', {'list': predictions})

def prediction_detail(request):
    pass