from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import *
from django.contrib.auth.decorators import login_required
from .utils import send_to_mail, generate_code


def sign_up_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Such a user exists. Please log in')
                return redirect('login')
            form.save()
            messages.success(request, 'Successfully authorized. Log in')
            return redirect('login')
    form = SignUpForm()
    return render(request, 'account/sign_up.html', {'form':form})


def log_in_view(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Something went wrong...')

    form = LoginForm()
    return render(request, 'account/login.html', {'form':form})


def log_out_view(request):
    logout(request)
    messages.info(request, 'Logged out.')
    return redirect('sign_up')

@login_required(login_url='log_in')
def profile_view(request):
    user = User.objects.get(username=request.user.username)
    return render(request, 'account/profile.html', {'user':user})



def change_pass_view(request):
    if request.method == 'GET':
        code = generate_code()
        request.session['verification_code'] = code
        send_to_mail(request.user.email, code)
        messages.info(request, 'Verification code sent to your email')
        form = PassChangeForm()
        return render(request, 'account/change_pass.html', {'form':form})

    else:
        form = PassChangeForm(request.POST)
        if form.is_valid():
            old_pass = form.cleaned_data['old_pass']
            new_pass = form.cleaned_data['new_pass']
            code = form.cleaned_data['code']
            session_code = request.session.get('verification_code')
            if not request.user.check_password(old_pass):
                messages.error(request, 'YOur old password was entered wrongly')
                return redirect('change_pass')
            if session_code != code:
                messages.error(request, 'Verification code is wrong.')

            user = request.user
            user.set_password(new_pass)
            user.save()
            messages.success(request, 'Password changed successfully')
            return redirect('profile')


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'account/edit_profile.html', {'form': form})


