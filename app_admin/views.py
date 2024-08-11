from django.shortcuts import render
from bird_voice_classifier.models import Prediction, Feedback
from django.contrib.auth.models import User

# Create your views here.

def dashboard(request):
    prediction_count = Prediction.objects.all().count()
    feedback_count = Feedback.objects.all().count()
    user_count = User.objects.all().count()
    return render(request, 'app-admin/dashboard.html', {'prediction_count': prediction_count, 'feedback_count': feedback_count, 'user_count': user_count})

def user_list(request):
    users = User.objects.all()
    return render(request, 'app-admin/user-list.html', {'list': users})

def user_detail(request, username):
    user = User.objects.get(username = username)
    predictions_count = Prediction.objects.filter(user = user).count()
    predictions = Prediction.objects.filter(user = user)
    feedback_count = 0
    for prediction in predictions:
        if Feedback.objects.get(predictiion= prediction).exists():
            feedback_count += 1

    return render(request, 'app-admin/user-details.html', {'user': user, 'prediction_count': predictions_count, 'feedback_count': feedback_count, 'predictions': predictions})

def predications_list(request):
    predictions = Prediction.objects.all()
    return render(request, 'app-admin/predictions.html', {'list': predictions})

def prediction_detail(request, pid):
    prediction = Prediction.objects.get(id = pid)
    feedback = {}
    if Feedback.objects.get(predictiion = prediction).exists():
        feedback = Feedback.objects.get(predictiion = prediction)
    return render(request, 'app-admin/prediction-details.html', {'prediction': prediction, 'feedback': feedback})

def feedback_list(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'app-admin/feedback_list.html', {'list': feedbacks})