from django import forms
from django.contrib import admin
from django.contrib.admin.models import LogEntry

from .models import *


# Register your models here.

admin.site.site_header = 'Preguntas Frecuentes'
admin.site.index_title = 'Administración'
admin.site.site_title = 'Admin'

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 5

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text','id','question')
    list_filter = ('text','id','question')
    search_fields = ('text','id','question')


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 5

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text','id','categ')
    list_filter = ('text','id','categ')
    search_fields = ('text','id','categ')
    inlines = [AnswerInline]


class CategAdmin(admin.ModelAdmin):
    list_display = ('text', 'id')
    list_filter = ('text', 'id')
    search_fields = ('text', 'id')
    inlines = [QuestionInline]

class LogEntryAdminForm(forms.ModelForm):
    class Meta:
        model = LogEntry
        fields = (
            'user',
            'action_flag',
            'object_id',
            'object_repr',
            'change_message',
            'content_type'
        )
@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    actions = None
    list_display_links = None
    list_display = ('action_time','user','action_flag','__str__')
    search_fields = ('user__username', 'change_message')
    readonly_fields = (
        'action_time', 'user', 'action_flag', '__str__', 'content_type',
        'object_repr', 'change_message',)
    list_filter = ('action_flag',)
    exclude = ('object_id',)
    form = LogEntryAdminForm

admin.site.register(Categ, CategAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
