from os.path import splitext
from django.utils.text import slugify
def image_upload_to(instance, filename:str) -> str:
    base_filename, file_extension = splitext(filename)
    return f"post/images/{slugify(instance.post.title)}/{slugify(base_filename)}/{file_extension}"