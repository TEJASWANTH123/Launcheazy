# appname/urls.py
from django.urls import path,include
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('user_list/', views.user_list, name='user_list'),

]
