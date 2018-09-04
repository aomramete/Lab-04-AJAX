from django.contrib import admin
from tweets.models import Tweet
from django.contrib import admin
from tweets.models import Tweet,HashTag
# Register your models here.
admin.site.register(HashTag)
admin.site.register(Tweet)
