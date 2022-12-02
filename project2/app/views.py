from django.shortcuts import render

# Create your views here.
def name(request):
    d={'nam':'suma'}
    return render(request,'name.html',d)


def name(request):
    d={'a':20}
    return render(request,'name.html',d)