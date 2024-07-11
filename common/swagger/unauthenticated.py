from django.shortcuts import redirect
from django.urls import reverse


class RedirectLogin:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Define a list of paths to exclude from redirection
        excluded_paths = ['/api/', '/media/']  # Add other paths as needed

        if not request.user.is_authenticated and \
                request.path_info != reverse('login') and not \
                any(request.path_info.startswith(path) for path in excluded_paths):
            # Redirect to the login page if the user is not authenticated
            return redirect(reverse('login'))

        response = self.get_response(request)
        return response
