from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def home(request):
    jobs = Job.objects.all().order_by('-creationdate')[:4]
    return render(request, 'home.html', {'job': jobs})


def user_login(request):
    error = ""

    if request.method == "POST":
        uname = request.POST['uname']
        pwd = request.POST['pwd']

        user = authenticate(username=uname, password=pwd)

        if user is not None:
            try:
                user1 = UserProfile.objects.get(user=user)

                if user1.type == "student":
                    login(request, user)
                    error = "no"
                else:
                    error = "yes"

            except UserProfile.DoesNotExist:
                error = "yes"
        else:
            error = "yes"

    return render(request, "User_login.html", {"error": error})

def recruiter_login(request):
    error = ""

    if request.method == "POST":
        uname = request.POST['username']
        pwd = request.POST['password']

        user = authenticate(username=uname, password=pwd)

        if user is not None:
            try:
                user1 = Recruiter.objects.get(user=user)

                if user1.type == "recruiter" and user1.status!="pending":
                    login(request, user)
                    error = "no"
                else:
                    error = "not"

            except Recruiter.DoesNotExist:
                error = "yes"
        else:
            error = "yes"

    return render(request, "Recruiter_login.html", {"error": error})

def recruiter_register(request):
    error = ""

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        company_name = request.POST['company_name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        image = request.FILES.get('image')
        gender = request.POST['gender']


        try:
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )

            Recruiter.objects.create(
                user=user,
                mobile=phone,
                image=image,
                gender=gender,
                company=company_name,
                type="recruiter",   # ✅ FIXED
                status="pending"
            )

            error = "no"

        except Exception as e:
            print(e)
            error = "yes"

    return render(request, "Recruiter_register.html", {"error": error})

def recruiter_home(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
        
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    job_count = Job.objects.filter(recruiter=recruiter).count()
    app_count = Apply.objects.filter(job__recruiter=recruiter).count()
    
    context = {
        "job_count": job_count,
        "app_count": app_count,
        "recruiter": recruiter
    }
    return render(request, "recruiter_home.html", context)

def recruiter_profile(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    return render(request, "recruiter_profile.html", {"recruiter": recruiter})

def edit_recruiter_profile(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    
    error = ""
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        con = request.POST['contact']
        gen = request.POST['gender']
        com = request.POST['company']
        
        user.first_name = fn
        user.last_name = ln
        recruiter.mobile = con
        recruiter.gender = gen
        recruiter.company = com
        
        try:
            user.save()
            recruiter.save()
            error = "no"
        except:
            error = "yes"
            
        if 'image' in request.FILES:
            recruiter.image = request.FILES['image']
            recruiter.save()
            
    return render(request, "edit_recruiter_profile.html", {"error": error, "recruiter": recruiter})

def change_password_recruiter(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    
    error = ""
    if request.method == "POST":
        cp = request.POST['currentpassword']
        np = request.POST['newpassword']
        rp = request.POST['repeatpassword']
        
        user = request.user
        if user.check_password(cp):
            if np == rp:
                user.set_password(np)
                user.save()
                error = "no"
            else:
                error = "nismatch"
        else:
            error = "yes"
            
    return render(request, "change_password_recruiter.html", {"error": error})

def delete_job(request, pid):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
        
    job = Job.objects.get(id=pid)
    job.delete()
    return redirect('job_list')

def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
        
    user = request.user
    student = UserProfile.objects.get(user=user)
    app_count = Apply.objects.filter(student=student).count()
    
    return render(request, "user_home.html", {"app_count": app_count, "student": student})

def user_profile(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
        
    user = request.user
    student = UserProfile.objects.get(user=user)
    return render(request, "user_profile.html", {"student": student})

def edit_user_profile(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    
    error = ""
    user = request.user
    student = UserProfile.objects.get(user=user)
    
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        con = request.POST['contact']
        gen = request.POST['gender']
        
        user.first_name = fn
        user.last_name = ln
        student.mobile = con
        student.gender = gen
        
        try:
            user.save()
            student.save()
            error = "no"
        except:
            error = "yes"
            
        if 'image' in request.FILES:
            student.image = request.FILES['image']
            student.save()
            
    return render(request, "edit_user_profile.html", {"error": error, "student": student})

def change_password_user(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    
    error = ""
    if request.method == "POST":
        cp = request.POST['currentpassword']
        np = request.POST['newpassword']
        rp = request.POST['repeatpassword']
        
        user = request.user
        if user.check_password(cp):
            if np == rp:
                user.set_password(np)
                user.save()
                error = "no"
            else:
                error = "nismatch"
        else:
            error = "yes"
            
    return render(request, "change_password_user.html", {"error": error})

def admin_home(request):
    if not request.user.is_staff:
        return redirect('admin_login')
        
    user_count = UserProfile.objects.filter(type="student").count()
    recruiter_count = Recruiter.objects.all().count()
    pending_recruiter = Recruiter.objects.filter(status="pending").count()
    job_count = Job.objects.all().count()
    application_count = Apply.objects.all().count()
    
    context = {
        "user_count": user_count,
        "recruiter_count": recruiter_count,
        "pending_recruiter": pending_recruiter,
        "job_count": job_count,
        "application_count": application_count
    }
    return render(request, "admin_home.html", context)

def admin_view_jobs(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    
    jobs = Job.objects.all().order_by('-creationdate')
    return render(request, "admin_view_jobs.html", {"jobs": jobs})

def delete_job_admin(request, pid):
    if not request.user.is_staff:
        return redirect('admin_login')
    
    job = Job.objects.get(id=pid)
    job.delete()
    return redirect('admin_view_jobs')

def admin_view_applications(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    
    applications = Apply.objects.all().order_by('-applydate')
    return render(request, "admin_view_applications.html", {"applications": applications})

def delete_application_admin(request, pid):
    if not request.user.is_staff:
        return redirect('admin_login')
    
    app = Apply.objects.get(id=pid)
    app.delete()
    return redirect('admin_view_applications')

def Logout(request):
    logout(request)
    return redirect('home')

def change_password_admin(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    
    error = ""
    if request.method == "POST":
        cp = request.POST['currentpassword']
        np = request.POST['newpassword']
        rp = request.POST['repeatpassword']
        
        user = request.user
        if user.check_password(cp):
            if np == rp:
                user.set_password(np)
                user.save()
                error = "no"
            else:
                error = "nismatch"
        else:
            error = "yes"
            
    return render(request, "change_password_admin.html", {"error": error})

def admin_profile(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    
    return render(request, "admin_profile.html")

def edit_admin_profile(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    
    error = ""
    user = request.user
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        em = request.POST['email']
        
        user.first_name = fn
        user.last_name = ln
        user.email = em
        
        try:
            user.save()
            error = "no"
        except:
            error = "yes"
            
    return render(request, "edit_admin_profile.html", {"error": error})

def admin_login(request):
    error = ""

    if request.method == "POST":
        uname = request.POST.get('username')
        pwd = request.POST.get('password')

        user = authenticate(username=uname, password=pwd)

        if user is not None and user.is_staff:
            login(request, user)
            error = "no"
        else:
            error = "yes"

    return render(request, "Admin_login.html", {"error": error})

def user_register(request):
    error = ""

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        image = request.FILES.get('image')
        gender = request.POST['gender']

        try:
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )

            UserProfile.objects.create(
                user=user,
                mobile=phone,
                image=image,
                gender=gender,
                type="student"   # ✅ FIXED
            )

            error = "no"

        except Exception as e:
            print(e)
            error = "yes"

    return render(request, "User_register.html", {"error": error})

from django.shortcuts import render, redirect, get_object_or_404

def view_users(request):
    if not request.user.is_staff:
        return redirect('admin_login')

    users = UserProfile.objects.filter(type="student")

    return render(request, "admin_view_users.html", {"users": users})

def delete_users(request, pid):
    if not request.user.is_staff:
        return redirect('admin_login')

    # Get user profile
    user_profile = get_object_or_404(UserProfile, id=pid)

    # Delete related auth user also
    user_profile.user.delete()

    return redirect('view_users')

from datetime import date

def view_recruiters(request):
    if not request.user.is_staff:
        return redirect('admin_login')

    recruiters = Recruiter.objects.all()

    return render(request, "admin_view_recruiters.html", {"recruiters": recruiters})

def change_status(request, pid):
    if not request.user.is_staff:
        return redirect('admin_login')

    recruiter = Recruiter.objects.get(id=pid)

    if request.method == "POST":
        status = request.POST['status']
        recruiter.status = status
        recruiter.save()
        return redirect('view_recruiters')

    return render(request, "admin_change_status.html", {"recruiter": recruiter})

def delete_recruiter(request, pid):
    if not request.user.is_staff:
        return redirect('admin_login')

    recruiter = Recruiter.objects.get(id=pid)
    recruiter.user.delete()
    return redirect('view_recruiters')

def add_job(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')

    error = ""
    if request.method == "POST":
        jt = request.POST['jobtitle']
        sd = request.POST['startdate']
        ed = request.POST['enddate']
        sal = request.POST['salary']
        l = request.FILES['logo']
        exp = request.POST['experience']
        loc = request.POST['location']
        sk = request.POST['skills']
        des = request.POST['description']

        user = request.user
        recruiter = Recruiter.objects.get(user=user)

        try:
            Job.objects.create(recruiter=recruiter, start_date=sd, end_date=ed, title=jt, salary=sal, image=l, description=des, experience=exp, location=loc, skills=sk, creationdate=date.today())
            error = "no"
        except:
            error = "yes"
    return render(request, "add_job.html", {"error": error})

def job_list(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    job = Job.objects.filter(recruiter=recruiter)
    return render(request, "job_list.html", {"job": job})

def edit_job(request, pid):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')

    error = ""
    job = Job.objects.get(id=pid)

    if request.method == "POST":
        jt = request.POST['jobtitle']
        sd = request.POST['startdate']
        ed = request.POST['enddate']
        sal = request.POST['salary']
        exp = request.POST['experience']
        loc = request.POST['location']
        sk = request.POST['skills']
        des = request.POST['description']

        job.title = jt
        job.start_date = sd
        job.end_date = ed
        job.salary = sal
        job.experience = exp
        job.location = loc
        job.skills = sk
        job.description = des

        try:
            job.save()
            error = "no"
        except:
            error = "yes"
        
        if 'logo' in request.FILES:
            job.image = request.FILES['logo']
            job.save()

    return render(request, "edit_job.html", {"error": error, "job": job})

def latest_jobs(request):
    job = Job.objects.all().order_by('-creationdate')
    return render(request, "latest_jobs.html", {"job": job})

def user_latestjobs(request):
    job = Job.objects.all().order_by('-creationdate')
    user = request.user
    student = UserProfile.objects.get(user=user)
    
    # Check if student has applied for these jobs
    applied_jobs = Apply.objects.filter(student=student).values_list('job_id', flat=True)
    
    return render(request, "user_latestjobs.html", {"job": job, "applied_jobs": applied_jobs})

def job_detail(request, pid):
    job = Job.objects.get(id=pid)
    return render(request, "job_detail.html", {"job": job})

def apply_for_job(request, pid):
    if not request.user.is_authenticated:
        return redirect('user_login')

    error = ""
    job = Job.objects.get(id=pid)
    user = request.user
    student = UserProfile.objects.get(user=user)

    if request.method == "POST":
        resume = request.FILES['resume']
        try:
            Apply.objects.create(job=job, student=student, resume=resume, applydate=date.today())
            error = "no"
        except:
            error = "yes"
    
    return render(request, "apply_for_job.html", {"error": error, "job": job})

def applied_jobs(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    
    user = request.user
    student = UserProfile.objects.get(user=user)
    applications = Apply.objects.filter(student=student)
    return render(request, "applied_jobs.html", {"applications": applications})

def view_applications(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    jobs = Job.objects.filter(recruiter=recruiter)
    applications = Apply.objects.filter(job__in=jobs)
    return render(request, "view_applications.html", {"applications": applications})
