# from django.conf.urls import url
from . import views
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as vm

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
   # url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', vm.login, name='login'),
    url(r'^accounts/logout/$', vm.logout, name='logout', kwargs={'next_page': '/'}),
    # url(r'', include('blog.urls')),
]
