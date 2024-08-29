from rest_framework import serializers
from posts.models.category import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name"
        ]
        
        read_only_fields = ["id"]   