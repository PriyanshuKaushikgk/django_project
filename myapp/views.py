from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Contact, Blogs
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail.message import EmailMessage

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        fname = request.POST.get("name")
        femail = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("description")
        
        # Save the contact data to the database
        query = Contact(name=fname, email=femail, phoneNumber=phone, description=desc)
        query.save()

        # Prepare the email message
        from_email = settings.EMAIL_HOST_USER
        subject = f'Email from {fname}'
        message = f'User Email: {femail}\nUser Phone Number: {phone}\n\nQUERY: {desc}'
        recipient_list = ['priyanshukaushi6919@gmail.com']  # Replace with your desired email

        # Send the email
        email_message = EmailMessage(subject, message, from_email, recipient_list)
        email_message.send(fail_silently=False)

        # Display success message
        messages.info(request, "Thanks, For Reaching Us! We will get back to you soon.........")
        return redirect('/contact')

    return render(request, 'contact.html')

def handlelogin(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        pass1 = request.POST.get("pass1")
        myuser = authenticate(username=uname, password=pass1)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Successfully :)")
            return redirect('/')
        else:
            messages.success(request, "Invalid User!!")
            return redirect('/login')

    return render(request, 'login.html')

def signuphandle(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("pass1")
        confirmpassword = request.POST.get("pass2")

        if password != confirmpassword:
            messages.warning(request, "Password is Incorrect")
            return redirect('/signup')
        
        try:
            if User.objects.get(username=uname):
                messages.info(request, "UserName Is Already Exist !!")
                return redirect('/signup')
        except:
            pass

        try:
            if User.objects.get(email=email):
                messages.warning(request, "Email Is Already Exist !!")
                return redirect('/signup') 
        except:
            pass

        myuser = User.objects.create_user(uname, email, password)
        myuser.save()
        messages.success(request, "SignUp Successfully Please Login :)")
        return redirect('/login')        

    return render(request, 'signup.html')

def handlelogout(request):
    logout(request)
    messages.info(request, "Logout Success")
    return redirect('/login')

def handleBlog(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Hey just login and Use My Website...")
        return redirect('/login')
    allPosts = Blogs.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'blog.html', context)

def search(request):
    query = request.GET['search']
    if len(query) > 100:
        allPosts = Blogs.objects.none()
    else:
        allPostsTitle = Blogs.objects.filter(title__icontains=query)
        allPostsDescription = Blogs.objects.filter(description__icontains=query)
        allPosts = allPostsTitle.union(allPostsDescription)

    if allPosts.count() == 0:
        messages.warning(request, "No Search Results")
    params = {'allPosts': allPosts, 'query': query}

    return render(request, 'search.html', params)
