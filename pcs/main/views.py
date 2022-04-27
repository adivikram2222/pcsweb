from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the index .")
def about(request):
    return HttpResponse("Hello, world. You're at the about .")
def service(request):
    return HttpResponse("Hello, world. You're at the service .")
def contact(request):
    return HttpResponse("Hello, world. You're at the contact .")