from django.contrib import admin
from .models import Education

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('title', 'school', 'start_date', 'end_date')
    filter_horizontal = ('technologies',)  # Si quieres el widget horizontal
