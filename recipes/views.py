from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.contrib import messages
from guest_user.decorators import allow_guest_user
from .models import GuestProfile

# Create your views here.

def check_password(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        if password == settings.RECIPE_ACCESS_PASSWORD:
            response = redirect('recipes:home')
            response.set_cookie(
                settings.RECIPE_ACCESS_COOKIE_NAME,
                'true',
                max_age=settings.RECIPE_ACCESS_COOKIE_AGE
            )
            return response
        messages.error(request, 'Invalid password')
    return render(request, 'recipes/password_check.html')

@allow_guest_user
def set_nickname(request):
    if request.method == 'POST':
        nickname = request.POST.get('nickname', '').strip()
        if nickname:
            profile, created = GuestProfile.objects.get_or_create(user=request.user)
            profile.nickname = nickname
            profile.save()
            messages.success(request, 'Nickname set successfully!')
            return redirect('recipes:home')
        messages.error(request, 'Please enter a nickname')
    return render(request, 'recipes/set_nickname.html')

@allow_guest_user
def home(request):
    return render(request, 'recipes/home.html')
