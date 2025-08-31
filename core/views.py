from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.contrib import messages

from user_profile.models import Profile

def home(request):
    return render(request, 'core/home.html', {
        'title': 'Home'
    })

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # a backend authenticated credentails.
            auth.login(request, user)
            messages.success(request, 'Login sucessful!')
            print("Login sucessful!")
            return redirect('core:home')
        else:
            # no backend authenticated credentails.
            messages.error(request, 'Invalid credentials, please check again')
            print("Invalid credentials, please check again")
            return redirect('core:signin')


    return render(request, 'core/signin.html', {
        'title': 'Signin'
    })

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'This email is already taken')
                print("this email is already taken")
                return redirect('core:signup')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'This username is already taken' )
                print("this user name is already taken")
                return redirect('core:signup')
            else:
                new_user = User.objects.create_user(first_name = first_name, last_name=last_name, username=username, email=email, password=password)
                new_user.save()
                # log the user using the credentails
                user_credentails = auth.authenticate(username=username, password=password)
                auth.login(request, user_credentails)
                # create a profile for the new user
                get_new_user = User.objects.get(username = username)
                new_profile = Profile.objects.create(user = get_new_user)
                new_profile.save()
                #redirect the user to homepage
                messages.success(request, 'The account is successfully created!')
                print("the account is successfully created!")
                return redirect('core:home')

        else:
            messages.error(request, "The passwords don't match" )
            print("the passwords don't match")
            return redirect('core:signup')
    return render(request, 'core/signup.html', {
        'title': 'Signup'
    })

def signout(request):
    auth.logout(request)
    messages.success(request, 'Logout successfully!' )
    print("Logout successfully!")
    return redirect('core:signin')