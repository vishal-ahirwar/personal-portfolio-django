from django.shortcuts import render

def Home(request):
    return render(request,"personal_portfolio/home.html")
