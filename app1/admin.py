from django.contrib import admin
from .models import Member
class MemberAdmin(admin.ModelAdmin):
    list_display="firstName","lastName"



admin.site.register(Member,MemberAdmin)




