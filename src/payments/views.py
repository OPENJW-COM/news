from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import SubscriptionPlan
# import stripe # Would be used in actual implementation

# stripe.api_key = settings.STRIPE_SECRET_KEY # Done at app startup ideally

@login_required
def list_plans(request):
    plans = SubscriptionPlan.objects.filter(is_active=True).order_by('price')
    context = {
        'plans': plans,
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
    }
    return render(request, 'payments/list_plans.html', context)

@login_required
def create_checkout_session(request, plan_id):
    # This is a conceptual placeholder for creating a Stripe Checkout session
    # A real implementation would:
    # 1. Get the plan object.
    # 2. Create a Stripe Checkout Session:
    #    session = stripe.checkout.Session.create(...)
    # 3. Redirect to Stripe or return session ID for Stripe.js
    plan = SubscriptionPlan.objects.get(id=plan_id) # Add error handling
    # For now, just redirect to a success placeholder or back to plans
    print(f"User {request.user.username} attempting to subscribe to {plan.name}")
    print("Stripe Checkout Session creation logic would go here.")
    # In a real scenario, you'd get a session_id from Stripe and redirect or use Stripe.js
    # return redirect(session.url, code=303) # Example redirect
    return redirect('payments:payment_success_placeholder') # Placeholder redirect

@login_required
def payment_success_placeholder(request):
    # Page shown after a conceptual successful payment or redirect from Stripe
    return render(request, 'payments/payment_success.html')

@login_required
def payment_cancel_placeholder(request):
    # Page shown if user cancels payment on Stripe's page
    return render(request, 'payments/payment_cancel.html')

# Webhook handler - CRITICAL for production
# from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse
# @csrf_exempt
# def stripe_webhook(request):
#     # ... webhook verification and event handling logic ...
#     return HttpResponse(status=200)
