from django.shortcuts import render

# Create your views here.
def home(request):
    name = "umesh !!!!"
    return render(request,'home.html',{ 'name': name})


def add(request):


    val1 = int(request.POST["num1"])
    val2 = int(request.POST["num2"])
    val = val1+val2
    
    return render(request,"result.html",{'vals':val})
   