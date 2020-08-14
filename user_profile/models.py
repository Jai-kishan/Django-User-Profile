from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BaseContent(models.Model):
    ACTIVE_CHOICES  = ((0, 'Inactive'), (2, 'Active'),)
    active          = models.PositiveIntegerField(choices=ACTIVE_CHOICES,default=2)
    created         = models.DateTimeField(auto_now_add=True)
    modified        = models.DateTimeField(auto_now=True)
    class Meta:
        abstract    = True

from django.core.exceptions import ValidationError
def validate_image(image):
    file_size = image.file.size
    limit = 2
    if file_size > limit * 1024 *1024:
        raise ValidationError("Max size of file is %s MB" % limit)

GENDER = ((0,'Male'),(1,'Female'),(2,'Other'))
class UserProfile(BaseContent):
    user            = models.OneToOneField(User,on_delete=models.CASCADE)
    birth_date      = models.DateField(null=True, blank=True)
    profile_pic     = models.ImageField(upload_to='user_pic/%Y/%m/%d', default='user_pic/no-img.jpg', blank=True, null=True, validators=[validate_image]) 
    contact         = models.CharField(max_length =15, null=True, blank=True)
    secondary_email = models.EmailField(max_length=150,null=True, blank=True)
    gender          = models.IntegerField(default=0,choices=GENDER)
    def __str__(self):
        return str(self.user.email)    