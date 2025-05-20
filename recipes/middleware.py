from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings
from django.contrib import messages

class RecipeAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Skip middleware for password check view and static files
        if request.path.startswith('/static/') or request.path == reverse('recipes:check_password'):
            return self.get_response(request)

        # Check if user has access
        has_access = request.COOKIES.get(settings.RECIPE_ACCESS_COOKIE_NAME)
        
        if not has_access and request.path.startswith('/recipes/'):
            messages.warning(request, 'Please enter the access password to view recipes.')
            return redirect('recipes:check_password')
            
        return self.get_response(request) 