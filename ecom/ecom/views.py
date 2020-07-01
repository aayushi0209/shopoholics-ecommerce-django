from django.shortcuts import render


# METHODS***************************************************************************************************************

def index(request):
    return render(request,'home.html')
