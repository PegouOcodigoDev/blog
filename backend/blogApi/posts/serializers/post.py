from rest_framework import serializers
from posts.models.post import Post
from posts.models.category import Category
from posts.serializers.image import ImagePostSerializer


class PostSerializer(serializers.ModelSerializer):
    images = ImagePostSerializer(many=True, required=False)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.filter().all())

    class Meta:
        model = Post
        fields = [
            "id", "category", "author", "images", "title", "slug", "content", 
            "likes", "status", "created_at", "updated_at", "comment_count"
        ]
        read_only_fields = ["id", "author", "created_at", "updated_at", "likes", "comment_count"]
        