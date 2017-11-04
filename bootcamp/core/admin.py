from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.translation import ugettext_lazy as _
##from .models import *
from bootcamp.activities.models import *
from bootcamp.articles.models import *
from bootcamp.messenger.models import *
from bootcamp.questions.models import *

from django.http import HttpResponse


from django.contrib import admin
admin.autodiscover()


admin.site.register(Activity)
admin.site.register(Notification)
admin.site.register(Article)
admin.site.register(ArticleComment)
##admin.site.register(Profile)
##admin.site.register(Feed)
admin.site.register(Message)
admin.site.register(Question)
admin.site.register(Answer)
