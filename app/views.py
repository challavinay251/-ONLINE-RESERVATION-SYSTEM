# app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserSignupForm, UserLoginForm, ReservationForm, CancellationForm
from .models import User, Reservation

def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:login')  # Redirect to login page after successful signup
    else:
        form = UserSignupForm()
    return render(request, 'app/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('app:reservation')  # Redirect to reservation form after successful login
    else:
        form = UserLoginForm()
    return render(request, 'app/login.html', {'form': form})

def reservation(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ReservationForm(request.POST)
            if form.is_valid():
                reservation = form.save(commit=False)
                reservation.user = request.user
                reservation.save()
                return redirect('app:reservation')
        else:
            form = ReservationForm()
        return render(request, 'app/reservation.html', {'form': form})
    else:
        return redirect('app:login')  # Redirect to login page if user is not authenticated

def cancellation(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CancellationForm(request.POST)
            if form.is_valid():
                pnr_number = form.cleaned_data['pnr_number']
                # Process cancellation logic here
                return redirect('app:reservation')
        else:
            form = CancellationForm()
        return render(request, 'app/cancellation.html', {'form': form})
    else:
        return redirect('app:login')  # Redirect to login page if user is not authenticated
