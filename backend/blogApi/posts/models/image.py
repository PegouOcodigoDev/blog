from django.db import models
from posts.models.post import Post
from posts.utils.file_utils import image_upload_to

class ImagePost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to=image_upload_to)
    
    def __str__(self) -> str:
        return f"Image for {self.post.title}"
    
    class Meta:
        db_table = "image"