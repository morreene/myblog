from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-
 
# Create your models here.
 
class Tag(models.Model):
    tag_name = models.CharField('tags', max_length=50)
    tag_cn_name = models.CharField('chinesename', max_length=50, blank=True)
 
    def __unicode__(self):
        return self.tag_name
 
 
class Article(models.Model):
    title = models.CharField('title', max_length=100)
    tag = models.ManyToManyField(Tag, max_length=50, blank=True)
    date_time = models.DateTimeField('date', auto_now_add=True)
    content = models.TextField('content', blank=True, null=True)
 
    def __unicode__(self):
        return self.title
 
    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'article'
        ordering = ['-date_time'] 