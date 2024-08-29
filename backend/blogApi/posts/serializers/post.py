from rest_framework import serializers
from posts.models.post import Post,ImagePost
from posts.serializers import category 

class ImagePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagePost
        fields = ["id", "image"]
        read_only_fields = ["id"] 


class PostSerializer(serializers.ModelSerializer):
    images = ImagePostSerializer(many=True, required=False)
    category = category.CategorySerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = [
            "id", "category", "author", "images", "title", "slug", "content", 
            "likes", "status", "created_at", "updated_at", "comment_count"
        ]
        read_only_fields = ["id", "author", "created_at", "updated_at", "likes", "comment_count"]

    def create(self, validated_data):
        print("Dados validados: %s", validated_data)

        category_data = validated_data.pop('category', None)
        images_data = validated_data.pop('images', None)
        
        print("Categoria: %s", category_data)
        print("Imagens: %s", images_data)

        post = Post.objects.create(**validated_data)

        if category_data:
            category_instance = category.Category.objects.get(id=category_data['id'])
            post.category = category_instance

        if images_data:
            for image in images_data:
                image.ImagePost.objects.create(post=post, **image)

        post.save()
        return post