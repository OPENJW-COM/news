from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from core_app.models import Website # To list user's websites on profile

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Log the user in directly after registration
            return redirect('user_management:profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user_management/register.html', {'form': form})

@login_required
def profile(request):
    user_websites = Website.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'user_management/profile.html', {'user_websites': user_websites})
