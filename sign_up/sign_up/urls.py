from django.conf.urls import patterns, include, url

from django.contrib import admin
from cmdb import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sign_up.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', views.index),
    url(r'^$', views.hello),
)
