from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'mi_app/index.html')