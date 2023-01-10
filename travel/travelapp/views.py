from django.http import HttpResponse
from django.shortcuts import render
from . models import Place,Team_members
# Create your views here.
def demo(request):
    # return HttpResponse("Hello World..!")
    name="Dhanya"
    # return render(request,'index_1.html',{'kname':name})
    obj=Place.objects.all()
    team=Team_members.objects.all()
    return render(request,'index.html',{'result':obj,'team_members':team})
def about(request):
    return render(request,'about.html')
def contact(request):
    return HttpResponse("Am contact")
def addition(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    res=x+y
    return render(request,'result.html',{"result":res})
