from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
def driver(request):
    return render(request, 'driver.html')