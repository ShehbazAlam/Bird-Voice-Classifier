import json
from django.shortcuts import render
from bird_voice_classifier.models import Prediction, Feedback
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

# Define the decorator
def superuser_required(view_func):
    return user_passes_test(lambda user: user.is_superuser)(view_func)

# Create your views here.
@login_required(login_url= '/auth/login')
@superuser_required
def dashboard(request):
    prediction_count = Prediction.objects.all().count()
    feedback_count = Feedback.objects.all().count()
    user_count = User.objects.all().count()
    return render(request, 'app-admin/dashboard.html', {'prediction_count': prediction_count, 'feedback_count': feedback_count, 'user_count': user_count})

@login_required(login_url= '/auth/login')
@superuser_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'app-admin/user-list.html', {'list': users})

@login_required(login_url= '/auth/login')
@superuser_required
def user_detail(request, username):
    user = User.objects.get(username = username)
    predictions_count = Prediction.objects.filter(user = user).count()
    predictions = Prediction.objects.filter(user = user)
    feedback_count = 0
    for prediction in predictions:
        if Feedback.objects.filter(predictiion= prediction).exists():
            feedback_count += 1

    return render(request, 'app-admin/user-details.html', {'user': user, 'prediction_count': predictions_count, 'feedback_count': feedback_count, 'predictions': predictions})

@login_required(login_url= '/auth/login')
@superuser_required
def predications_list(request):
    predictions = Prediction.objects.all()
    return render(request, 'app-admin/predictions.html', {'list': predictions})

@login_required(login_url= '/auth/login')
@superuser_required
def prediction_detail(request, pid):
    prediction = Prediction.objects.get(id = pid)
    with open('bird_image_links.json', mode='r') as f:
            bird_img_file = json.load(f)
    bird_img = bird_img_file[prediction.result]
    feedback = {}
    if Feedback.objects.filter(predictiion = prediction).exists():
        feedback = Feedback.objects.get(predictiion = prediction)
    return render(request, 'app-admin/prediction-details.html', {'prediction': prediction, 'feedback': feedback, 'bird_img': bird_img})

@login_required(login_url= '/auth/login')
@superuser_required
def feedback_list(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'app-admin/feedback_list.html', {'list': feedbacks})