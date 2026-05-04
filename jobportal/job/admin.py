from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(Recruiter)
admin.site.register(Job)
admin.site.register(Apply)