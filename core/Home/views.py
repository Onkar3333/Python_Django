from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def Home(request):

    peoples=[
        {"name" :"Onkar" , "Age": 17},
        {"name" :"om" , "Age": 13},
        {"name" :"Sandip" , "Age": 27},
        {"name" :"Sangram" , "Age": 23},
        {"name" :"Amir" , "Age": 14},
        {"name" :"Lalu Yadav" , "Age": 56},
        {"name" :"Narendra Modi" , "Age": 18},

    ]
     
    return render(request , "home/index.html" , context={'peoples' : peoples , 'page': "This is Django First Try"})

def about(request):
    context = {'page': "About_Us"}
    return render(request , "home/about.html",context)

def contact(request):
    context = {'page': "Contact_Us"}
    return render(request , "home/contact.html",context)


def success_page(request):
    return HttpResponse("This is a Success Page!")