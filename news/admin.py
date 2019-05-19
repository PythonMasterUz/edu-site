from django.contrib import admin

from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','is_published','date_published']

admin.site.register(News,NewsAdmin)
#admin.site.register()