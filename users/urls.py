from django.urls import path
from users import views as user_views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

app_name = 'users'
urlpatterns = [ 
    path(r'', user_views.profile, name = 'profile'),
    path('signup/', user_views.register,name='register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'user/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'user/logout.html') ,name='logout'),
    path('terms/', user_views.terms_condition, name='terms'),
]