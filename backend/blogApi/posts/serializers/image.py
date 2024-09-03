from posts.models.image import ImagePost
from posts.models.post import Post
from rest_framework import serializers

class ImagePostSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.filter().all())
    image = serializers.ImageField()
    
    class Meta:
        model = ImagePost
        fields = ["id", "post", "image"]
        read_only_fields = ["id"] 