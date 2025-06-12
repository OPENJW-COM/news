from django.urls import path
from . import views

app_name = 'core_app'
urlpatterns = [
    path('site/<int:website_id>/', views.view_website, name='view_website'),
]
