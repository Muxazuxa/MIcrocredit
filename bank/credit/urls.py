from django.conf.urls import url, include
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name='credit'

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name='credit/login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='credit/logout.html'), name='logout'),
    url(r'^customers/$', views.CustomerListView.as_view(), name='customer_list'),
]