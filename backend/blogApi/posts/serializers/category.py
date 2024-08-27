from rest_framework import serializers
from posts.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name"
        ]
        
        def validate_name(self, name:str):
            name.strip()
            if not name or name == "":
                raise serializers.ValidationError("O nome não pode ser vazio.")
            if len(name) < 3:
                 raise serializers.ValidationError("O nome deve conter mais de 3 caracteres.")
            
            return name