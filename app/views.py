from django.shortcuts import render
from app.models import GeneralInfo
from django.db import connection


def write_sql_queries_to_file(file_path):
    with open(file_path, 'w') as file:
        for query in connection.queries:
            file.write(f"{query.get('sql', '')}\n\n")


def index(request):
    general_info = GeneralInfo.objects.first()
    print(f"general_info :  {general_info.location}")
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
    }
    return render(request, 'index.html', context)


def about_us(request):
    all_records = GeneralInfo.objects.all()
    file_path = 'sql_queries.txt'
    write_sql_queries_to_file(file_path)
    context = {'records': all_records}
    return render(request, 'about_us.html', context)