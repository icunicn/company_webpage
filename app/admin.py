from django.contrib import admin
from app.models import GeneralInfo, service, Testimonial, FrequentlyAskedQuestion, ContactFormLog, Blog, Author
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


@admin.register(service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["tittle", "description"]
    search_fields = ["tittle"]


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = [
        "username", 
        "user_job", 
        "display_rating_count",
    ]

    def display_rating_count(self, obj):
        return '*' * obj.rating_count
    
    display_rating_count.short_description = "Rating"

@admin.register(FrequentlyAskedQuestion)
class FrequentlyAskedQuestionAdmin(admin.ModelAdmin):
    list_display = ["question"]
    search_fields = ["question"]
    fieldsets = (
        (None, {
            'fields': ('question', 'answer')
        }),
    )

@admin.register(ContactFormLog)
class ContactFormLogAdmin(admin.ModelAdmin):
    list_display = ['email', 'action_time', 'is_success', 'is_error']
    
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request):
        return False
    
    def has_delete_permission(self, request):
        return False

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'country', 'joined_date']
    

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'blog_image', 'created_at']
    
    