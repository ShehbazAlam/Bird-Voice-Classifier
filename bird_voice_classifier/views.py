from django.shortcuts import render

class site():
    def __init__(self) -> None:
        pass

    #function to presict the sound
    def predict(sound):
        pass

    #function to review prediction
    def review_prediction(user, review):
        pass


def login(request):
    return render(request, 'site/login.html')

def signup(request):
    return render(request, 'site/signup.html')

def index(request):
    return render(request, 'site/index.html')