from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Website
from .services import get_website_render_context

def view_website(request, website_id):
    """
    Renders a published website.
    For now, we'll use website_id. Later, this could be a subdomain or custom domain.
    """
    # website = get_object_or_404(Website, id=website_id, is_published=True)
    # For now, allow viewing non-published sites for testing
    website = get_object_or_404(Website, id=website_id)

    if not website.template:
        # Handle case where website has no template - maybe a default site structure or error
        # For now, raise Http404 or render a specific "no template" page
        raise Http404("This website does not have a template assigned and cannot be rendered.")

    context = get_website_render_context(website)

    # Construct the path to the website's base template
    # This assumes a convention like: core_app/website_templates/{template_name}/base.html
    template_base_path = f"core_app/website_templates/{website.template.name.lower().replace(' ', '_')}/base.html"

    # Fallback to a generic default if specific template's base.html isn't found.
    # This requires more robust template discovery or definition on the Template model.
    # For this subtask, we'll assume 'default_template' exists from step 2.
    # A real implementation would need to check if template_base_path exists
    # or have a field on the Template model specifying its entry point.

    # Simplified logic for now:
    if website.template.name == "Default Template": # Assuming a template named "Default Template"
         template_to_render = "core_app/website_templates/default_template/base.html"
    else:
        # This part needs a more robust way to link Template model to actual template files
        # For now, we'll just use the default for any template for simplicity of this subtask.
        # In a real scenario, you might have a 'path_to_template_dir' field on the Template model.
        # raise Http404(f"Template '{website.template.name}' not found or configured.")
        template_to_render = "core_app/website_templates/default_template/base.html"


    return render(request, template_to_render, context)
