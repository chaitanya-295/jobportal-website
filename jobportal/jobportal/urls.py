"""
URL configuration for jobportal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from job.views import *
from job import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('', views.home, name='home'),
    path('user_login/', views.user_login, name="user_login"),
    path('recruiter_login/', views.recruiter_login, name='recruiter_login'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('user_register/', views.user_register, name='user_register'),
    path('user_home/', views.user_home, name='user_home'),
    path('recruiter_register/', views.recruiter_register, name='recruiter_register'),
    path('recruiter_home/', views.recruiter_home, name='recruiter_home'),
    path('Logout/', views.Logout, name='Logout'),
    path('admin_view_users/', views.view_users, name='view_users'),
    path('delete_user/<str:pid>/', views.delete_users, name='delete_user'),
    path('view_recruiters/', views.view_recruiters, name='view_recruiters'),
    path('change_status/<str:pid>/', views.change_status, name='change_status'),
    path('delete_recruiter/<str:pid>/', views.delete_recruiter, name='delete_recruiter'),
    path('add_job/', views.add_job, name='add_job'),
    path('job_list/', views.job_list, name='job_list'),
    path('edit_job/<str:pid>/', views.edit_job, name='edit_job'),
    path('latest_jobs/', views.latest_jobs, name='latest_jobs'),
    path('user_latestjobs/', views.user_latestjobs, name='user_latestjobs'),
    path('job_detail/<str:pid>/', views.job_detail, name='job_detail'),
    path('apply_for_job/<str:pid>/', views.apply_for_job, name='apply_for_job'),
    path('applied_jobs/', views.applied_jobs, name='applied_jobs'),
    path('view_applications/', views.view_applications, name='view_applications'),
    path('admin_view_jobs/', views.admin_view_jobs, name='admin_view_jobs'),
    path('delete_job_admin/<str:pid>/', views.delete_job_admin, name='delete_job_admin'),
    path('admin_view_applications/', views.admin_view_applications, name='admin_view_applications'),
    path('delete_application_admin/<str:pid>/', views.delete_application_admin, name='delete_application_admin'),
    path('admin_profile/', views.admin_profile, name='admin_profile'),
    path('edit_admin_profile/', views.edit_admin_profile, name='edit_admin_profile'),
    path('change_password_admin/', views.change_password_admin, name='change_password_admin'),
    path('recruiter_profile/', views.recruiter_profile, name='recruiter_profile'),
    path('edit_recruiter_profile/', views.edit_recruiter_profile, name='edit_recruiter_profile'),
    path('change_password_recruiter/', views.change_password_recruiter, name='change_password_recruiter'),
    path('delete_job/<str:pid>/', views.delete_job, name='delete_job'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('edit_user_profile/', views.edit_user_profile, name='edit_user_profile'),
    path('change_password_user/', views.change_password_user, name='change_password_user'),
    
]

if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
