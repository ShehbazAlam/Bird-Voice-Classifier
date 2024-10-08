from django.shortcuts import render, redirect
from model import predict
from .forms import FileUploadForm
from django.core.files.storage import FileSystemStorage
from .models import Prediction, Feedback
from django.contrib.auth.decorators import login_required

import json

import random
import string

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def upload_file_to_dir(file):
    fs = FileSystemStorage()
    BASE_URL = "http://127.0.0.1:8000/"
    dir = './uploads'
    file_name = 'upload-'+generate_random_string(5)+'.mp3'
    file_path = f'{dir}/{file_name}'
    filename = fs.save(file_path, file)
    uploaded_file_url = fs.url(filename)

    return uploaded_file_url

def add_prediction_record(file, user, result):
    new_prediction = Prediction(user= user, file = file, result = result['prediction'], confidence = result['confidence'])
    new_prediction.save()
    return new_prediction.id

def index(request):
    form = FileUploadForm
    return render(request, 'site/index.html', {"form": form})

@login_required(login_url= '/auth/login')
def result(request):
    if request.method == "POST" and request.FILES['bird-sound']:
        file = request.FILES['bird-sound']
        uploaded_file_url = upload_file_to_dir(file)
        prediction = predict.prediction('.' + uploaded_file_url)
        
        with open('bird_image_links.json', mode='r') as f:
            bird_img_file = json.load(f)
        bird_img = bird_img_file[prediction['prediction'].replace('_sound', '')]
        prediction.update({'bird_img': bird_img, 'prediction': prediction['prediction'].replace('_sound', '')})
        pid = add_prediction_record(user= request.user, file= uploaded_file_url, result= prediction)
        return render(request, 'site/result.html', {'prediction': prediction, 'prediction_id': pid, 'audio': '.'+ uploaded_file_url})
        
    else:
        return render(request, 'site/result.html')


def feedback(request):
    if request.method == "POST":
        pid = request.POST['prediction']
        review = request.POST['review']
        desc = request.POST['desc']
        correction = request.POST['correction']

        parent = Prediction.objects.get(id = pid)
        new_feedback = Feedback(predictiion = parent, review= review, desc= desc, correction= correction)
        new_feedback.save()
        
        message ="Thank You for your feedback"

        return render(request, 'site/index.html', {'message': message})
    
    return redirect('')
    