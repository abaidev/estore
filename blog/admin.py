from django.contrib import admin
from .models import PostTag, Post, PostImage, PostComment, PostCategory

admin.site.register(PostTag)

@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']

class PostImageStacked(admin.StackedInline):
    model = PostImage

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']
    inlines = [PostImageStacked]

admin.site.register(PostComment)

