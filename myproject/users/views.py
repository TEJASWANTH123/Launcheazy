from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm, UserLoginForm
from .models import CustomUser  # Import your custom user model
import logging
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

logger = logging.getLogger(__name__)

def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'user_list.html', {'users': users})
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = form.save()  # Save the user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Log in the user
                return redirect('login')  # Redirect to the login page
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                # Authentication failed, so display an error message
                form.add_error(None, 'Invalid username or password. Please try again.')

    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})



