from django.shortcuts import render

# Create your views here.

def indexView(request):
    context = {}
    return render(request, 'inicio.html', context=context)