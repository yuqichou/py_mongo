# coding:utf8

from django import forms
from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField


class StringListField(forms.CharField):
    def prepare_value(self, value):
        return ', '.join(value)
    
    def to_python(self, value):
        if not value:
            return []
        return [item.strip() for item in value.split(',')]



class CategoryField(ListField):
    def formfield(self, **kwargs):
        return models.Field.formfield(self, StringListField, **kwargs)

class Post(models.Model):
    title = models.CharField(max_length=100)
    categories = CategoryField()
    
    
    
    
    
    
    
    
    
class ObjectListField(forms.CharField):
    def prepare_value(self, value):
        if not value:
            return ''

        newvalue = {}
        for key, val in value.__dict__.items():
            if type(val) is unicode:
                newvalue[key] = val

        return ", ".join(["%s=%s" % (k, v) for k, v in newvalue.items()])

    def to_python(self, value):
        if not value:
            return {}

        obj = {}
        lst = [item.strip() for item in value.split(',')]
        for item in lst:
            val = item.split('=');
            obj[val[0]] = val[1]
        
        return obj 
    
    
# Subclass EmbeddedModelField to make it wok with admin edit
class EmbedOverrideField(EmbeddedModelField):
    def formfield(self, **kwargs):
        return models.Field.formfield(self, ObjectListField, **kwargs)

# Create your models here.
class User(models.Model):
    name = EmbedOverrideField('Name',help_text='Make sure you are passing a string of this value: key=val, key=val, ...etc')
    email = models.EmailField(max_length=255, db_index=True)
    def __unicode__(self):
        return '%s %s (%s)' % (self.name.fn, self.name.ln, self.email)

class Name(models.Model):
    fn = models.CharField(max_length=50)
    ln = models.CharField(max_length=50)
    def __unicode__(self):
        return '%s %s' % (self.fn, self.ln)
    
    
    
    
    
    
    
    