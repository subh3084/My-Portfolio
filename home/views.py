from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from matplotlib.style import context
from home.models import Contact

# Create your views here.

def home(request):
    # return HttpResponse("this is home page(/) by SUBHANSHU")
    context={'name':'SUBHANSHU'}
    return render(request,'home.html',context)       # here we have passed the python dictionary to home.html

def about(request):
    # return HttpResponse("this is about page(/about) ")
    details={'name':'SUBHANSHU' , 'college':'Chandigarh University', 'course1':'MCA','grade1':84,
             'graduation':'Delhi University','course2':'BSC', 'grade2':77,
             'school':'Army Public School','place':'Dhaula Kuan, Delhi', 'grade3':83
            }
    return render(request,'about.html',details)

def projects(request):
    # return HttpResponse("this is project page(/project)")
    information={'p_name':'Django', 'By':'SUBHANSHU'}
    return render(request,'projects.html',information)
    
def contact(request):
    if request.method=="POST":

        name= request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']
        # print(name,email,phone,desc)
        ins=Contact(name=name, email=email , phone=phone , desc=desc)
        ins.save()
        print("Date has been written to the DB")

    # return HttpResponse("this is contact page(/contact)")
    # info={'p_no':'8800XXXXXX', 'address':'Delhi'}
    return render(request,'contact.html')