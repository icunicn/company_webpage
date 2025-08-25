from django.shortcuts import render, redirect
from django.core.mail import send_mail
from app.models import GeneralInfo, service, Testimonial, FrequentlyAskedQuestion, ContactFormLog, Blog, Author
from django.utils import timezone
from django.db import connection
from django.conf import settings
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def write_sql_queries_to_file(file_path):
    with open(file_path, 'w') as file:
        for query in connection.queries:
            file.write(f"{query.get('sql', '')}\n\n")


def index(request):
    general_info = GeneralInfo.objects.first()
    services = service.objects.all()
    testimonials = Testimonial.objects.all()
    faqs = FrequentlyAskedQuestion.objects.all()
    recent_blogs = Blog.objects.all().order_by('-created_at')[:5]
    for blog in recent_blogs:
        print(f"Blog Title: {blog.title}, Author: {blog.author.first_name if blog.author else 'Unknown'}, Created At: {blog.created_at}")
    context = {
        'company_name': general_info.company_name,
        'location': general_info.location,
        'phone': general_info.phone,
        'opening_hours': general_info.opening_hours,
        'email': general_info.email,
        'video_url': general_info.video_url,
        'twitter_url': general_info.twitter_url,
        'instagram_url': general_info.instagram_url,
        'facebook_url': general_info.facebook_url,
        'linkedin_url': general_info.linkedin_url,

        'services': services,
        'testimonials': testimonials,
        'faqs': faqs,
        'recent_blogs': recent_blogs,
    }
    return render(request, 'index.html', context)

def contact_form(request):
    if request.method == 'POST':
        print("\nUser has submitted contact form")
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')


    is_success = False
    is_error = False
    eror_message = ""
    # send email()
    try:
        send_mail(
            subject = subject,
            message = f"Name: {name}\nEmail: {email}\nMessage: {message}",
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [settings.EMAIL_HOST_USER],
            fail_silently = False,
        )
    except Exception as e:
        is_error = True
        eror_message = str(e)
        messages.error(request, "An error occurred while sending your message. Please try again later.")
    else:
        is_success = True

        messages.success(request, "Your message has been sent successfully!")
    
    ContactFormLog.objects.create(
        name=name,
        email=email,
        subject=subject,
        message=message,
        action_time=timezone.now(),
        is_success=is_success,
        is_error=is_error,
        error_message=eror_message
    )
    return redirect('Home')

def about_us(request):
    all_records = GeneralInfo.objects.all()
    file_path = 'sql_queries.txt'
    write_sql_queries_to_file(file_path)
    context = {'records': all_records}
    return render(request, 'about_us.html', context)

def blog_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    general_info = GeneralInfo.objects.first()

    context = {
        "blog": blog,
        "is_blog_page": True,  # Flag to indicate we're on a blog page
        # include site-wide info used by header/main
        "company_name": general_info.company_name if general_info else 'Company',
        "location": general_info.location if general_info else '',
        "phone": general_info.phone if general_info else '',
        "opening_hours": general_info.opening_hours if general_info else '',
        "email": general_info.email if general_info else '',
        "video_url": general_info.video_url if general_info else '',
        "twitter_url": general_info.twitter_url if general_info else '',
        "instagram_url": general_info.instagram_url if general_info else '',
        "facebook_url": general_info.facebook_url if general_info else '',
        "linkedin_url": general_info.linkedin_url if general_info else '',
    }
    return render(request, 'blog_details.html', context)

def blog_list(request):
    general_info = GeneralInfo.objects.first()
    blogs = Blog.objects.all().order_by('-created_at')
    
    # Get unique categories for filtering
    categories = Blog.objects.values_list('category', flat=True).distinct()
    categories = [c for c in categories if c]  # Remove empty categories
    
    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(blogs, 9)  # Show 9 blogs per page
    
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    
    context = {
        'blogs': blogs,
        'categories': categories,
        'is_blog_page': True,  # Add this flag
        'company_name': general_info.company_name if general_info else 'Company',
        'location': general_info.location if general_info else '',
        'phone': general_info.phone if general_info else '',
        'opening_hours': general_info.opening_hours if general_info else '',
        'email': general_info.email if general_info else '',
        'video_url': general_info.video_url if general_info else '',
        'twitter_url': general_info.twitter_url if general_info else '',
        'instagram_url': general_info.instagram_url if general_info else '',
        'facebook_url': general_info.facebook_url if general_info else '',
        'linkedin_url': general_info.linkedin_url if general_info else '',
    }
    
    return render(request, 'blog.html', context)