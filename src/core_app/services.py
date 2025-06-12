from .models import Website, Template, SiteModule, User

def create_new_website(user: User, website_name: str, template: Template = None, initial_modules_data: list = None):
    """
    Creates a new website for a given user.
    Optionally assigns a template and creates initial modules.
    """
    if not website_name:
        raise ValueError("Website name cannot be empty.")

    website = Website.objects.create(
        user=user,
        name=website_name,
        template=template
    )

    if initial_modules_data:
        for i, module_data in enumerate(initial_modules_data):
            SiteModule.objects.create(
                website=website,
                module_type=module_data.get('module_type', 'text'), # Default to text
                content_data=module_data.get('content_data', {}),
                order=i
            )

    return website

def get_website_render_context(website: Website):
    """
    Prepares the context needed to render a website.
    This will fetch the website's modules and prepare them for rendering.
    """
    modules = website.modules.all().order_by('order')

    # This part is conceptual and will need refinement.
    # We need a way to map module_type to its specific HTML template.
    # For now, we'll just pass the module objects.
    processed_modules = []
    for module in modules:
        # Example: module_template_name = f"module_templates/{module.module_type}.html"
        # This assumes you have such files.
        processed_modules.append({
            "instance": module,
            "content_data": module.content_data,
            # This is a placeholder for how a module would find its template
            "template_path": f"core_app/module_templates/{module.module_type}.html"
        })

    return {
        "website": website,
        "modules": processed_modules,
    }
