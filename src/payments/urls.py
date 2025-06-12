from django.urls import path
from . import views

app_name = 'payments'
urlpatterns = [
    path('plans/', views.list_plans, name='list_plans'),
    path('checkout/<int:plan_id>/', views.create_checkout_session, name='create_checkout_session'),
    path('success/', views.payment_success_placeholder, name='payment_success_placeholder'),
    path('cancel/', views.payment_cancel_placeholder, name='payment_cancel_placeholder'),
    # path('webhooks/stripe/', views.stripe_webhook, name='stripe_webhook'),
]
