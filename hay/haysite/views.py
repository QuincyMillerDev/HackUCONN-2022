from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'hay/main.html', context)
    
def question(request):
    context = {}
    return render(request, 'hay/question.html', context)

def tellMore(request):
    context = {}
    return render(request, 'hay/tell-more.html', context)
# Create your views here.
