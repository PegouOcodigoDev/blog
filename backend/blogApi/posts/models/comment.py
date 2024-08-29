from django.db import models
from users.models import User
from posts.models.post import Post

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"Comment by {self.author.name} on {self.post.title}"
    
    class Meta:
        db_table = "comment"
        ordering = ["-created_at"]