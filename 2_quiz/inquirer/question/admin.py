from django.contrib import admin
from question.models import Choice
from question.models import Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question']}),]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
