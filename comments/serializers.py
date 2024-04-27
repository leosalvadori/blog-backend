from rest_framework import serializers
from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['user', 'post']

    def get_user(self, obj):
        return obj.user.username
