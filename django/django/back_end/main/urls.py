from django.conf import settings
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.index , name='home'),
    path('about/', views.about, name='about'),
    path('classes/', views.classes,name='classes'),
    path('schedules/', views.schedules,name='schedules'),
    path('contactus/', views.contactus, name='contactus'),
    path('signup/', views.signup, name='signup'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(),{'next_page': settings.LOGOUT_REDIRECT_URL},name='logout'),

]
