from posts.models import Category
from posts.serializers.category import CategorySerializer
from posts.views.base import GenericListCreateAPIView, GenericRetrieveUpdateDestroyAPIView

class CategoryList(GenericListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(GenericRetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer