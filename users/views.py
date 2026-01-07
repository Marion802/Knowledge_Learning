from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth import login

from .models import User
from .forms import UserRegistrationForm, UserLoginForm


def activate_account(request, token):
    """
    Activates a user account using a unique activation token.

    When the user clicks on the activation link received by email,
    their account is marked as active.
    """
    user = get_object_or_404(User, activation_token=token)
    user.is_active = True
    user.save()

    return HttpResponse("Account successfully activated.")

def register(request):
    """
    Handles user registration.

    Creates a new inactive user account and sends an activation
    email containing a unique activation link.
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            user.send_activation_email()
            return render(
                request,
                'users/registration_success.html'
            )
    else:
        form = UserRegistrationForm()

    return render(
        request,
        'users/register.html',
        {'form': form}
    )



def user_login(request):
    """
    Authenticates and logs in a user.

    If the credentials are valid, the user is logged in
    and redirected to the home page.
    """
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return redirect('home')
    else:
        form = UserLoginForm()

    return render(
        request,
        'users/login.html',
        {'form': form}
    )
