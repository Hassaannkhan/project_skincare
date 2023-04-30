from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Skincaredata)
class searchadmin(admin.ModelAdmin):
    list_display = ('uname','email')
    search_fields = ('uname','email')
    # fields = ('fname',)
    list_filter = ('uname','email')