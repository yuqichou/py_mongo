from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from apps.news.urls import news_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'py_mongo.views.home', name='home'),
    # url(r'^py_mongo/', include('py_mongo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     
     (r'^news/', include(news_urlpatterns)),
     
#     url(r'^news/posts', 'apps.news.views.find_posts'),
     
)
