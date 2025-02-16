from django.contrib import admin
from .models import Technologies

# Register your models here.

class TechnologiesAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')


admin.site.register(Technologies, TechnologiesAdmin)