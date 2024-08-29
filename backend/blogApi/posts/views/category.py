from posts.models.category import Category
from posts.serializers.category import CategorySerializer
from posts.views.base import GenericListCreateAPIView, GenericRetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter

class CategoryList(GenericListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter]
    search_fields = ["name"]


class CategoryDetail(GenericRetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer