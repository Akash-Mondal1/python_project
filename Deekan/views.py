from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable":"this is sent"
    }
    return render(request, 'index.html', context)
    #return HttpResponse("this is home page")

def About(request):
    return render(request, 'About.html')

def Courses(request):
    return render(request, 'Courses.html')
def Contact(request):
    return render(request, 'Contact.html')