from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def service(request):
    return render(request,'service.html')
def educational(request):
    return render(request,'educational.html')
def base(request):
    return render(request,'base.html')
def registeration(request):
    return render(request,'registeration.html')
def login(request):
    return render(request,'login.html')
def dashboard(request):
    return render(request,'dashboard.html')
def itservices(request):
    return render(request,'itindex.html')
            