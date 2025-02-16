from django.shortcuts import render
from .models import Education
# Create your views here.

def home(request):
    education = Education.objects.all()
    return render(request, 'home/home.html', {'education':education})