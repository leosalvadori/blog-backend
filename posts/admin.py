from django.contrib import admin
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'username', 'status', 'deleted', 'created_at')

    def username(self, obj):
        return obj.user.username
