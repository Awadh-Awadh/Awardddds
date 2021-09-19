from django.shortcuts import render

# Create your views here.
def home(request):
    title = "Awadh"
    return render(request,'projects/home.html', {'title':title})