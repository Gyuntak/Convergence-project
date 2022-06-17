from django.contrib import admin

# Register your models here.
from mzroad.models import BigData
from mzroad.models import AI

admin.site.register(BigData)
admin.site.register(AI)