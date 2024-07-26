from django.shortcuts import render
from model import predict
from .forms import FileUploadForm
from django.core.files.storage import FileSystemStorage

import os

import random
import string

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def index(request):
    form = FileUploadForm
    return render(request, 'site/index.html', {"form": form})

def result(request):
    if request.method == "POST" and request.FILES['bird-sound']:
        file = request.FILES['bird-sound']
        
        fs = FileSystemStorage()
        BASE_URL = "http://127.0.0.1:8000/"
        dir = './static/uploads'
        file_name = 'upload-'+generate_random_string(5)+'.mp3'
        file_path = f'{dir}/{file_name}'
        filename = fs.save(file_path, file)
        uploaded_file_url = fs.url(filename)
        prediction = predict.prediction('.' + uploaded_file_url)

        print(prediction)
        return render(request, 'site/result.html', {'prediction': prediction})
        
    else:
        return render(request, 'site/result.html')
