from django.shortcuts import redirect, render
from .forms import UserRegistration
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout


def registerUser(request):
    if request.method=='POST':
        form = UserRegistration(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = make_password(form.cleaned_data['password'])
     
            user = User.objects.create_user(username=username, email=email, password=password)

            if user:
                instance = form.save(commit=False)
                instance.user = user
                instance.save()
                return redirect('postList')

    else:
        form = UserRegistration()
        return render(request, 'users/register.html', {'form':form})
    

def loginUser(request):
    if request.method == 'POST': ## if the submit button is clicked
        username = request.POST.get('username')  #get username
        password = request.POST.get('password')  #get password
        user = authenticate(request, username=username, password=password) 

        if user is not None:
            login(request,user)
            return redirect('postList')
        else:
            return redirect('login')
        
    return render(request, 'users/login.html')