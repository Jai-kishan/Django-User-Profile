from django import template
from user_profile.models import UserProfile
from django.shortcuts import get_object_or_404

register = template.Library()


@register.simple_tag
def ger_user_profile(user_id):
    user_data= get_object_or_404(UserProfile, user=user_id)
    return user_data
    # pass