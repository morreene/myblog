from django.contrib import admin

# Register your models here.

from blog.models import Tag, Article
 
# Register your models here.
 
admin.site.register(Tag)
admin.site.register(Article)