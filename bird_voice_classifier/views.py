from django.shortcuts import render
from model import predict
from .forms import FileUploadForm
from django.core.files.storage import FileSystemStorage
from .models import Prediction

import os

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
    new_prediction = Prediction(user = user, file = file, result = result['prediction'], confidence = result['confidence'])
    new_prediction.save()

def index(request):
    form = FileUploadForm
    return render(request, 'site/index.html', {"form": form})

def result(request):
    if request.method == "POST" and request.FILES['bird-sound']:
        file = request.FILES['bird-sound']
        uploaded_file_url = upload_file_to_dir(file)
        prediction = predict.prediction('.' + uploaded_file_url)
        print(prediction['prediction'])
        add_prediction_record(user= request.user, file= file, result= prediction)
        return render(request, 'site/result.html', {'prediction': prediction})
        
    else:
        return render(request, 'site/result.html')
