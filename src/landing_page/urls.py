from django.urls import path
from . import views

app_name = 'landing_page'
urlpatterns = [
    path('', views.home_page, name='home'),
    path('features/', views.features_page, name='features'),
    # path('pricing/', views.pricing_page, name='pricing'),
]
