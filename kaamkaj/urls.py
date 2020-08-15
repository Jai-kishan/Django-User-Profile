from django.urls import path
from .views import *


urlpatterns =[
	# path('signup/', signup_user, name='signup'),
	path('', kaamkaj, name='kaamkaj'),
	# path('logout/', logout_user, name='logout'),
	# path('login/', login_user, name='login'),
	path('create/', create_kaam, name='create_kaam'),
	path('todos/', kaam_list, name='kaamkaj_list'),
	path('todo/<int:todo_id>', kaamkaj_details, name='kaam_details'),
	path('todo/<int:todo_pk>/complete/', kaamkaj_complete, name='kaam_complete'),
]