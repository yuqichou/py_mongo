# coding:utf8
from apps.news.models import Post
from django.http import HttpResponse
from django.core import serializers


def find_posts(request):
    jsonData=serializers.serialize("json", Post.objects.all(),ensure_ascii=False)
    return HttpResponse(jsonData)