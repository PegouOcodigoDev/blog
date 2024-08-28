from rest_framework import serializers
from posts.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    
    post = serializers.PrimaryKeyRelatedField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "post", "author", "content", "created_at"]

        read_only_fields = ["id", "created_at", "author"]
