from rest_framework import serializers
from posts.models import ImagePost

class ImagePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagePost
        fields = ["id", "post", "image",]
        read_only_fields = ["id", "post"] 
