from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.

def register(request):
    if request.method == 'POST':
        fname=request.POST["first_name"]
        lname=request.POST["last_name"]
        username=request.POST["user_name"]
        email=request.POST['email']
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        if password1 == password2:
            user = User.objects.create_user(username = username, password = password1, email = email, first_name = fname, last_name = lname)
            user.save();
            print('User Created')
        
        else:
            print('Both password fieds should be same')
        return redirect('/')

    else:
        return render(request, 'accounts/register.html')

