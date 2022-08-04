from django.shortcuts import render
from portfolio.models import Project
def Home(request):
    projects=Project.objects.all()
    return render(request,"personal_portfolio/home.html",{"projects":projects})
