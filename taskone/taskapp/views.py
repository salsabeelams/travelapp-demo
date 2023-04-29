from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import team
# Create your views here.
def home(request):
    obj = place.objects.all()
    team_obj = team.objects.all()
    return render(request,'index.html',{'result':obj,'tresult':team_obj})
def about(request):
    return HttpResponse("Hello ,This is About page")
def contact(request):
    return render(request,'contact.html')
def details(request):
    return render(request,'details.html')
def thanks(request):
    return HttpResponse("Thanks for visiting this site")