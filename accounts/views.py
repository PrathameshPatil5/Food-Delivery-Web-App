from django.shortcuts import render,redirect
from django.contrib.auth import authenticate , login ,logout
from .models import Customuser

# Create your views here.
def register_view(request):
    if request.method=='POST':
        data=request.POST
        print(data)
        Customuser.objects.create_user(username=data['username'],password=data['password'],role=data['role'])
        return redirect('login') #here login is url name
    return render(request,"register.html") # here it is template name

def login_view(request):
    if request.method == 'POST':
        data=request.POST
        print(data)
        username=data['username']
        password=data['password']
        user=authenticate(request,username=username,password=password)   #authenticate() → checks if the username/password are correct.

        if user is not None:
            login(request,user)          
                            # HOW LOGIN WORKS
                            #2. How login actually works behind the scenes
                            # When you type your username & password:

                            # Authenticate
                            # Django runs authenticate(username, password) to check if:

                            # This username exists in the database.

                            # The password matches the stored (hashed) password.

                            # If correct → create a session
                            # Django stores your user ID in a session cookie in your browser.

                            # This cookie is like a visitor pass.

                            # As long as you have it, Django knows who you are for every page you open.

                            # If wrong → error message
                            # No session is created, you remain “anonymous”.



            if  user.role=='customer':
                return redirect('customer') #it is url name
            elif user.role=="restaurant":
                return redirect('restaurant')
        else :
            return render(request,'login.html',{'error':'invalid_credential'})
    return render (request,'login.html')
      
        
    
    
def logout_view(request):
    logout(request)

    return redirect('login')




