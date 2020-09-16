from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    dict1 = {"variable":"This is test tag"}
    return render(request, 'index.html',context=dict1)

def about(request):
    return HttpResponse ("This is ABout page")

def services(request):
    return HttpResponse ("This is services page")    

def contact(request):
    return HttpResponse ("This is contact page")

def support_heroes(request):
    return render(request, 'support_heroes.html',)

def carry_heroes(request):
    return render(request, 'carry_heroes.html',)