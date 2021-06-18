from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fncode(request):
    return HttpResponse("code iam rahil")
def fnsample(request):
    return render(request,'sample.html')       
