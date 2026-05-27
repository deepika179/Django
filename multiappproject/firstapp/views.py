from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view1(request):
    a="This is the response from the first app"
    return HttpResponse(a)
