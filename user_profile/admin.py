from django.contrib import admin
from user_profile.models import *
# Register your models here.

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name','parent','order']
#     list_filter = ('name',)

@admin.register(UserProfile)
class UserProfileDataAdmin(admin.ModelAdmin):
    list_display = ['id','user_id','user','birth_date','profile_pic',]
    list_filter = ('user', 'birth_date')

# @admin.register(UserVerification)
# class UserVerificationAdmin(admin.ModelAdmin):
#     list_display = ['user','verified','hash_key']
#     list_filter = ('user',)

# @admin.register(MasterLookUp)
# class MasterLookUpAdmin(admin.ModelAdmin):
#     list_display = ['id','name','parent','code','order']
#     list_filter = ('name',)

# @admin.register(UserSubscription)
# class UserSubscriptionAdmin(admin.ModelAdmin):
#     list_display = ['user','master_data','active']
#     list_filter = ('user',)


# @admin.register(Location)
# class LocationAdmin(admin.ModelAdmin):
#     list_display = ['id','name','parent','code','order']
#     list_filter = ('name',)

# @admin.register(SocialMediaLink)
# class SocialMediaLinkAdmin(admin.ModelAdmin):
#     list_display = ['user','master_data','active','url']
#     list_filter = ('user',)

# @admin.register(UserEducation)
# class UserEducationAdmin(admin.ModelAdmin):
#     list_display = ['user','college','type_of_degree','broad_stream','certificate_course']
#     list_filter = ('user',)

# @admin.register(UserWork)
# class UserWorkAdmin(admin.ModelAdmin):
#     list_display = ['user','company','role','industry']
#     list_filter = ('user',)