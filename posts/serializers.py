from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['user']


class PostStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['status']
        read_only_fields = ['content', 'created_at', 'deleted', 'id', 'title', 'user']
