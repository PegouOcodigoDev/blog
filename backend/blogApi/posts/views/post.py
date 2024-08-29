from posts.models.post import Post
from posts.serializers.post import PostSerializer
from posts.views.base import GenericListCreateAPIView, GenericRetrieveUpdateDestroyAPIView
from django.core.exceptions import PermissionDenied
from rest_framework.filters import SearchFilter
from posts.utils.pagination import CustomPagination

class PostList(GenericListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [SearchFilter]
    search_fields = ["title"]
    pagination_class = CustomPagination
    

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(GenericRetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_update(self, serializer):
        post = self.get_object()
        if post.author != self.request.user:
            raise PermissionDenied({"detail": "Você não tem autorização para atualizar esse post."})
        serializer.save()

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied({"detail": "Você não tem autorização para deletar esse post."})
        instance.delete()