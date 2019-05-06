from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'credit'

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name='credit/login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='credit/logout.html'), name='logout'),

    # Customer_url
    url(r'^customers/$', views.CustomerListView.as_view(), name='customer_list'),
    url(r'^customers/add/$', views.CustomerCreateView.as_view(), name='customer_add'),
    url(r'^customers/update/(?P<pk>\d+)/$', views.CustomerUpdateView.as_view(), name='customer_update'),

    # Credit url
    url(r'^credits/$', views.CreditListView.as_view(), name='credit_list'),
    url(r'^credit/add/(?P<pk>\d+)/$', views.CreditCreateView.as_view(), name='credit_add'),
    # Graphic url
    url(r'^credit/cut/(?P<pk>\d+)/$', views.GraphicCreateView.as_view(), name='graphic_add'),
    url(r'^graphics/$', views.GraphicListView.as_view(), name='graphic_list'),
    url(r'^graphic/(?P<pk>\d+)/$', views.CreditGraphicView.as_view(), name='graphic')

]