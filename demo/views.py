from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'demo/home.html')

def add(request):
    fname=request.POST["first_name"]
    lname=request.POST["last_name"]
    name=fname+" "+lname
    email=request.POST['email']
    usrd=[{'name':name,
            'email':email}
            
            ]
    context={
            'result':usrd}
    return render(request, 'demo/user_data.html', context=context)