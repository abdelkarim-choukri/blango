from django.contrib import admin
from blog.models import Tag, Post, Comment, AuthorProfile
# Register your models here.
admin.site.register(Tag)
admin.site.register(Comment)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",),"summary":("title",)}
    list_display = ('slug', 'published_at')

admin.site.register(Post, PostAdmin)
admin.site.register(AuthorProfile)
