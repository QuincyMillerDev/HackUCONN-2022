from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'hay/question.html', context)

# Create your views here.
