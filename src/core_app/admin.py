from django.contrib import admin
from .models import Template, Website, SiteModule

@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name', 'description')

# This class will be temporarily registered and then unregistered
# to be replaced by WebsiteAdminWithInlines
@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'template', 'is_published', 'created_at')
    list_filter = ('is_published', 'template', 'user')
    search_fields = ('name', 'user__username')
    raw_id_fields = ('user', 'template')

@admin.register(SiteModule)
class SiteModuleAdmin(admin.ModelAdmin):
    list_display = ('website', 'module_type', 'order', 'created_at')
    list_filter = ('module_type', 'website__name')
    search_fields = ('website__name',)
    # To make editing JSONField easier, consider django-jsoneditor or similar,
    # but for now, the default textarea will work.
    # For ordering, Django admin respects 'ordering' in Meta class of the model.

# To allow adding/editing SiteModules directly when editing a Website,
# you can define an inline:
class SiteModuleInline(admin.TabularInline): # or admin.StackedInline
    model = SiteModule
    extra = 1 # Number of empty forms to display
    # raw_id_fields = ('website',) # Not needed here as it's an inline to website

# Then, modify WebsiteAdmin to include it:
# Unregister the one possibly registered without inlines
admin.site.unregister(Website)
@admin.register(Website) # Re-register with inlines
class WebsiteAdminWithInlines(admin.ModelAdmin):
    list_display = ('name', 'user', 'template', 'is_published', 'created_at')
    list_filter = ('is_published', 'template', 'user')
    search_fields = ('name', 'user__username')
    raw_id_fields = ('user', 'template')
    inlines = [SiteModuleInline]
