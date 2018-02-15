from django.conf.urls import url

from . import views

urlpatterns = [
    # Main page
    url(r'^$', views.main, name='main'),

    # Pages
    url(r'^Account/$', views.account, name='Account'),
    url(r'^FindMentor/$', views.findMentor, name='FindMentor'),
    url(r'^FindMentee/$', views.findMentee, name='FindMentee'),

    # Logout
    url(r'^LogOut/$', views.logOut, name='logOut'),

    # For FindMentor AJAX-requests
    # url(r'^Ajax/GetUserData/$', views.ajax_GetUserData, name='ajax_GetUserData'),
    url(r'^Ajax/FindMentor/$', views.ajax_FindMentor, name='ajax_FindMentor'),
    url(r'^Ajax/ChosenMentor/$', views.ajax_ChooseMentor, name='ajax_ChooseMentor'),
]