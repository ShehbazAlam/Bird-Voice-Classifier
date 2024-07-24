from django.shortcuts import render
from model import predict
from .forms import FileUploadForm

def index(request):
    form = FileUploadForm
    return render(request, 'site/index.html', {"form": form})

def result(request):
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        file = request.FILES['bird-sound']
        
        prediction = predict.prediction(file)

        print(prediction)
        return render(request, 'site/result.html', {'prediction': prediction})
        
    else:
        return render(request, 'site/result.html')
