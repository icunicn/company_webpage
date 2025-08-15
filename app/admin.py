from django.contrib import admin
from app.models import GeneralInfo
# Register your models here.
@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'location', 'email', 'phone', 'opening_hours')
    search_fields = ('company_name', 'location', 'email')
    list_filter = ('location',)
    fieldsets = (
        (None, {
            'fields': ('company_name', 'location', 'email', 'phone')
        }),
        ('Social Media Links', {
            'fields': ('video_url', 'twitter_url', 'instagram_url', 'facebook_url', 'linkedin_url'),
            'classes': ('collapse',)
        }),
        ('Additional Information', {
            'fields': ('opening_hours',),
            'classes': ('collapse',)
        }),
    )

    # def has_add_permission(self, request):
    #     # Allow adding only one GeneralInfo instance
    #     if GeneralInfo.objects.exists() > 2:
    #         return False
    #     return super().has_add_permission(request)
    
    # def has_change_permission(self, request, obj=None):
    #     # Allow changing only the first GeneralInfo instance
    #     if obj and GeneralInfo.objects.count() > 1:
    #         return False
    #     return super().has_change_permission(request, obj)
    
    # def has_delete_permission(self, request, obj=None):
    #     # Prevent deletion of the GeneralInfo instance
    #     return False
