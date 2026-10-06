from django.shortcuts import render

def calculadora_view(request):
    return render(request, 'sumar/index.html')