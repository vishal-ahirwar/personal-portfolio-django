from django.shortcuts import render

# Create your views here.
from .models import Project
def Home(request):
    projects=Project.objects.all()
    return render(request,"personal_portfolio/home.html",{"projects":projects})
