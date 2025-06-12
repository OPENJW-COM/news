from django.db import models
from django.contrib.auth.models import User # Using Django's built-in User model

class Template(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    preview_image_url = models.URLField(blank=True, null=True)
    # For simplicity, we'll assume template files are stored elsewhere and referenced by name or path
    # Later, this could be a FileField or a reference to a directory structure.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Website(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='websites')
    template = models.ForeignKey(Template, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200) # A user-friendly name for the site
    # sub_domain = models.SlugField(unique=True, max_length=100) # e.g., mycompany.generator.com
    # custom_domain = models.CharField(max_length=255, blank=True, null=True, unique=True) # e.g., www.mycompany.com
    # For now, let's keep domain management simple and revisit later.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Placeholder for custom CSS, might move to a separate model or file later
    custom_css = models.TextField(blank=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} (Owner: {self.user.username})"

class SiteModule(models.Model):
    MODULE_TYPES = [
        ('text', 'Text Block'),
        ('image', 'Image'),
        ('gallery', 'Image Gallery'),
        ('video', 'Video'),
        ('html', 'Custom HTML'),
        ('contact_form', 'Contact Form'),
        # Add more module types as needed
    ]
    website = models.ForeignKey(Website, on_delete=models.CASCADE, related_name='modules')
    module_type = models.CharField(max_length=50, choices=MODULE_TYPES)
    # Using JSONField to store flexible content for different module types
    # Ensure your MySQL version supports JSONField (MySQL 5.7.8+)
    # Django automatically handles this for supported databases.
    content_data = models.JSONField(default=dict, blank=True)
    order = models.PositiveIntegerField(default=0) # To determine the order of modules on a page
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order'] # Default ordering for modules within a website

    def __str__(self):
        return f"{self.get_module_type_display()} module for {self.website.name}"
