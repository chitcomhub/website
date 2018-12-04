from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'datetime', 'pic', 'author')
        read_only_fields = ('datetime',)
