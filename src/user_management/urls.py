from django.urls import path, include
from . import views

app_name = 'user_management'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    # Include Django's built-in auth URLs (for login, logout, password management)
    # login is at /accounts/login/ by default if using django.contrib.auth.urls
    # We will define our own login url path that maps to Django's LoginView
    # and logout path.
    # For more control, we can define them explicitly:
    path('accounts/', include('django.contrib.auth.urls')), # provides login, logout, password_reset etc.
                                                          # login url is 'login', logout is 'logout'
                                                          # templates are expected in 'registration/' directory
]
