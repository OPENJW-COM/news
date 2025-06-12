from django.shortcuts import render

def home_page(request):
    return render(request, 'landing_page/home.html')

def features_page(request):
    return render(request, 'landing_page/features.html')

# Placeholder for pricing page if we decide to add it now
# def pricing_page(request):
#     return render(request, 'landing_page/pricing.html')
