from django.shortcuts import render, redirect
from .forms import SignUpForm, UserLoginForm
from .models import CustomUser  # Import your custom user model
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'user_list.html', {'users': users})

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password1']

            user = CustomUser(username=username,password=password)  # Create a user instance
            # user.set_password(password)  # Set the password
            user.save()  # Save the user to the database

            user = authenticate(request, username=username, password=password)
            return redirect('login')
            # if user is not None:
            #     login(request, user)  # Log in the user
            #     messages.success(request, 'You have successfully logged in.')
            #     return redirect('login')  # Redirect to the login page
        else:
            return render(request, 'signup.html', {'form': form, 'error_message': 'User not enrolled. Please try again.'})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('profile')
        else:
            # Authentication failed, so display an error message
            messages.error(request, 'Invalid username or password. Please try again.')

    form = {}  # You can remove the form variable if you're not using it

    return render(request, 'login.html', {'form': form})


# from your_app.models import CustomUser
# user = CustomUser(username='testuser', password='password')
# user.save()


