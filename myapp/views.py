from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Contact

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        fname =  request.POST.get("name")
        femail = request.POST.get("email")
        phone =  request.POST.get("phone")
        desc =  request.POST.get("description")
        # print(name,email,phone,desc)
        # return HttpResponse("Contact successfuully saved!!!!!!!!!!!!!!")
        query = Contact(name=fname,email=femail,phoneNumber=phone,description=desc)
        query.save()
        messages.info(request,"Thanks, For Reaching Us! We will get back You Soon.........")
        return redirect('/contact')

    return render(request,'contact.html')

def handlelogin(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        pass1 = request.POST.get("pass1")
        myuser = authenticate(username=uname,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Successfully :)")
            return redirect('/')
        else:
            messages.success(request,"Invalid User!!")
            return redirect('/login')


    return render(request,'login.html')


def signuphandle(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("pass1")
        confirmpassword = request.POST.get("pass2")
        # print(uname,email,password,confirmpassword)
        if password!=confirmpassword:
            messages.warning(request,"Password is Incorrect")
            return redirect('/signup')
        try:
            if User.objects.get(username=uname):
                messages.info(request,"UserName Is Already Exist !!")
                return redirect('/signup')
        except:
            pass

        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email Is Already Exist !!")
                return redirect('/signup') 
        except:
            pass


        myuser = User.objects.create_user(uname,email,password)
        myuser.save()
        messages.success(request,"SignUp Successfully Please Login :)")
        return redirect('/login')        
    return render(request,'signup.html')


def handlelogout(request):
    logout(request)
    messages.info(request,"Logout Success")
    return redirect('/login')







