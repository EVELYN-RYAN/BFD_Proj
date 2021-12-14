from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def indexPageView(request):
    return render(request, "bfdPages/index.html")


def aboutPageView(request):
    return render(request, "bfdPages/about.html")


def productPageView(request):
    return render(request, "bfdPages/products.html")


def createorderPageView(request) :
    return render(request, "createOrder/orderForm.html")

def blogPageView(request) :
    return render(request,"bfdpages/blogs.html")