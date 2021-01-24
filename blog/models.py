from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from account.models import Manager, User

class PostTag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class PostCategory(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField()
    cover = models.ImageField(upload_to='post-categories', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=500, db_index=True)
    slug = models.SlugField(max_length=500, default="")
    category = models.ForeignKey(PostCategory, on_delete=models.SET_NULL, null=True, default=None)
    tags = models.ManyToManyField(PostTag, default=None, blank=True, related_name='post_tags')
    content = RichTextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, verbose_name='Likes', default=None, blank=True, related_name='post_likes')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True) # allow non-english slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f"<ID: {self.id}> {self.title}. <AUTHOR: {self.author.user.username}>:"


# class PostLike(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     liked_person = models.ForeignKey(User, on_delete=models.CASCADE)


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts')
    main_img = models.BooleanField(verbose_name="Is Main Picture", default=False, null=True, blank=True)

    def __str__(self):
        return self.post.title + ".img"


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    comment = RichTextField()

    def __str__(self):
        return f"comment for {self.post.title}. ID {self.post.id}"
