from django.contrib import admin

from .models import Poll


class PollAdmin(admin.ModelAdmin):
    autocomplete_fields = ['article_name']

admin.site.register(Poll,PollAdmin)

"""
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    fieldsets = [
        (None, {'fields': ['question_text']}),
        (None, {'fields': ['article']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    readonly_fields = ['pub_date']
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
"""


