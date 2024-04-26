from django.contrib import admin
from comments.models import Comment


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ('username', 'post', 'deleted', 'created_at', 'comment')

    def username(self, obj):
        return obj.user.username
