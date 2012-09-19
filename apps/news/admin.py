# coding:utf8
from apps.news.models import User
from django.contrib.admin import site, ModelAdmin
from models import Post
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  #@UndefinedVariable





def categories(instance):
    return ', '.join(instance.categories)

class PostAdmin(ModelAdmin):
    list_display = ['title', categories]

site.register(Post, PostAdmin)
site.register(User)
