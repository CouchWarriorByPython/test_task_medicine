from django.contrib import admin
from .models import *


@admin.register(LineOfAction)
class LineOfActionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'slug')
    list_filter = ('title',)
    search_fields = ('id', 'title', 'slug')
    ordering = ['title']
    list_per_page = 5


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', 'surname', 'patronymic')}
    filter_horizontal = ['line_of_action']
    list_display = ('id', 'full_name', 'display_line_of_action', 'date_of_birth', 'work_experience', 'slug')
    list_filter = ('name', 'work_experience')
    search_fields = ('id', 'name', 'surname', 'slug', 'work_experience')
    ordering = ['name', 'work_experience']
    list_display_links = ['id', 'full_name']
    list_per_page = 5
