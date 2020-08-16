from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BaseContent(models.Model):
    ACTIVE_CHOICES = ((0, 'Inactive'), (2, 'Active'),)
    active = models.PositiveIntegerField(choices=ACTIVE_CHOICES,
                                         default=2)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        #-----------------------------------------#
        # Don't create a table in database
        # This table is abstract
        #--------------------ends here--------------------#
        abstract = True

    #                                        BaseContent
    def switch(self):   
        # Deactivate a model if it is active
        # Activate a model if it is inactive
        self.active = {2: 0, 0: 2}[self.active]
        self.save()

class KaamKaj(BaseContent):
	title 			= models.CharField(max_length=150)
	memo 			= models.TextField(blank=True)
	# created			= models.DateTimeField(auto_now_add=True)
	complete_date	= models.DateTimeField(null=True, blank=True)
	important 		= models.BooleanField(default=False)
	user 			= models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title