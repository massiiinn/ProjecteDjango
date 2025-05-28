from django.contrib import admin
from .models import Author, Tag, Post

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("tag",)
    search_fields = ("tag",)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date")
    search_fields = ("title", "content", "excerpt")
    list_filter = ("date", "tags")
    prepopulated_fields = {"slug": ("title",)}
