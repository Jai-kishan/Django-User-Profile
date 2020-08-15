from django.contrib import admin
from kaamkaj.models import *
# Register your models here.

class KaamKajAdmin(admin.ModelAdmin):
	readonly_fields=('created',)

admin.site.register(KaamKaj,KaamKajAdmin)