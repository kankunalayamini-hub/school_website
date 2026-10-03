
from django.shortcuts import render,redirect
from app.models import *
from app.models import *
from app.forms import *


def homeview(request):
    return render(request, 'app/home.html')

def aboutview(request):
    return render(request, 'app/about.html')

def VIIIclassview(request):
    return render(request, 'app/VIIIclass.html')

def IXclassview(request):
    return render(request, 'app/IXclass.html')

def Xclassview(request):
    return render(request, 'app/Xclass.html')

def photosview(request):
    return render(request, 'app/photos.html')

def videosview(request):
    return render(request, 'app/videos.html')

def parent_regview(request):
    if request.method == 'POST':
        form = Parent_regForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('table') 
    else:
        form = Parent_regForm()
    return render(request, "app/parent_reg.html", {"f": form})


def latest_newsview(request):
    return render(request, 'app/latest_news.html')

def contactview(request):
    if request.method == 'POST':
        form = Student_regForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('table') 
    else:
        form = Student_regForm()
    return render(request, 'app/contact_us.html', {'fo': form})

def tableview(request):
    parents = Parent.objects.all()
    students = Student.objects.all()
    return render(request, 'app/table.html', {
        'p': parents,
        's': students,
    })

def Dataview(request):
    return render(request, 'app/data.html')


    
    
    

