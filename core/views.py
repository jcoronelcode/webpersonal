from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, 'core/about-me.html')

def contact(request):
    return render(request, 'core/contact.html')

