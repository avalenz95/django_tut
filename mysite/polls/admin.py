from django.contrib import admin

from .models import Question

#Registers Polls question as editable in admin dashboard
admin.site.register(Question)