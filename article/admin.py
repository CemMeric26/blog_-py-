from django.contrib import admin

from .models import Article,Comment,TakenCourse,Video,TakenCourseVideo
from polls.models import Poll
# Register your models here.

admin.site.register(Comment)
admin.site.register(Poll)
admin.site.register(TakenCourse)
admin.site.register(Video)
admin.site.register(TakenCourseVideo)
#admin.site.register(Question)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["title","author","created_date"]

    list_display_links= ["title","created_date"]

    search_fields = ["title"]

    list_filter = ["created_date"]

    class Meta:
        model = Article
