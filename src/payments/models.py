from django.db import models
from django.contrib.auth.models import User
# from core_app.models import Template # If plans unlock specific templates

class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=100, unique=True)
    stripe_plan_id = models.CharField(max_length=100, unique=True,
                                      help_text="ID of the plan in Stripe")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')
    description = models.TextField(blank=True)
    features = models.JSONField(default=list, blank=True,
                               help_text="List of features for this plan")
    # e.g., max_websites, access_premium_templates, etc.
    is_active = models.BooleanField(default=True) # So plans can be retired

    def __str__(self):
        return f"{self.name} (${self.price}/{self.currency})"

class UserSubscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='subscription')
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.SET_NULL, null=True)
    stripe_subscription_id = models.CharField(max_length=100, unique=True, blank=True, null=True)
    stripe_customer_id = models.CharField(max_length=100, unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=False) # True if current period paid
    current_period_start = models.DateTimeField(null=True, blank=True)
    current_period_end = models.DateTimeField(null=True, blank=True)
    cancel_at_period_end = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s subscription to {self.plan.name if self.plan else 'N/A'}"
