from django.contrib import admin
from skifflog.models import Block

admin.site.register(Block, admin.ModelAdmin)
