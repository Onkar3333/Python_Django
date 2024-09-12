from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def recepies(request):
    
    if request.method == "POST":
        data=request.POST

        Receipe_name = data.get('Receipe_name')
        Receipe_desc = data.get('Receipe_desc')
        Receipe_image = request.FILES.get('Receipe_image')

        # print(Receipe_name)
        # print(Receipe_desc)
        # print(Receipe_image)

        Receipe.objects.create(
            Receipe_name = Receipe_name,
            Receipe_desc = Receipe_desc,
            Receipe_image = Receipe_image,
        )
        return redirect('/recepies/')
        

    queryset = Receipe.objects.all()
    context = {'receipes' : queryset}    
    return render(request, 'recepies.html' , context)


def delete_receipe(request,id):
    
    return redirect('/recepies/')