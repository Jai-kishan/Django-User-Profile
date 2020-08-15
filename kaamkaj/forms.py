from django.forms import ModelForm
from .models import *

class  TodoForm(ModelForm):
	class Meta:
		model  = KaamKaj
		fields = ('title', 'memo', 'important')