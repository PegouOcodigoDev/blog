from posts.models import ImagePost
from posts.serializers.image_post import ImagePostSerializer
from posts.views.base import GenericListCreateAPIView, GenericRetrieveUpdateDestroyAPIView
from django.core.exceptions import PermissionDenied

class ImagePostList(GenericListCreateAPIView):
    queryset = ImagePost.objects.all()
    serializer_class = ImagePostSerializer


class ImagePostDetail(GenericRetrieveUpdateDestroyAPIView):
    queryset = ImagePost.objects.all()
    serializer_class = ImagePostSerializer

    def perform_update(self, serializer):
        image_post = self.get_object()
        if image_post.post.author != self.request.user:
            raise PermissionDenied({"detail": "Você não tem autorização para atualizar essa imagem."})
        serializer.save()

    def perform_destroy(self, instance):
        if instance.post.author != self.request.user:
            raise PermissionDenied({"detail": "Você não tem autorização para deletar essa imagem."})
        instance.delete()