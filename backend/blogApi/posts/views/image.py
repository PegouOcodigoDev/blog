from posts.models.image import ImagePost
from posts.serializers.image import ImagePostSerializer
from posts.views.base import GenericListCreateAPIView, GenericRetrieveUpdateDestroyAPIView

class ImagePostList(GenericListCreateAPIView):
    queryset = ImagePost.objects.all()
    serializer_class = ImagePostSerializer


class ImagePostDetail(GenericRetrieveUpdateDestroyAPIView):
    queryset = ImagePost.objects.all()
    serializer_class = ImagePostSerializer