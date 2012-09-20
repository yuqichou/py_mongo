from django.conf.urls.defaults import patterns, url



news_urlpatterns = patterns(
    '',
    url(r'^posts/', 'apps.news.views.find_posts'),              
)
