from posts.models import Comment
from posts.serializers.comment import CommentSerializer
from posts.views.base import GenericListCreateAPIView, GenericRetrieveUpdateDestroyAPIView
from django.core.exceptions import PermissionDenied

class CommentList(GenericListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentDetail(GenericRetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_update(self, serializer):
        comment = self.get_object()
        if comment.author != self.request.user:
            raise PermissionDenied({"detail": "Você não tem autorização para atualizar esse comentário."})
        serializer.save()

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied({"detail": "Você não tem autorização para deletar esse comentário."})
        instance.delete()