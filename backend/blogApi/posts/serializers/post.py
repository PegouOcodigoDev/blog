from rest_framework import serializers
from posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id", "category", "author", "title", "slug", "content", 
            "likes", "status", "created_at", "updated_at", "comment_count"
        ]
        

        read_only_fields = ["id", "created_at", "updated_at", "likes", "comment_count"]