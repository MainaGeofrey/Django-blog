from django.contrib import admin
from .models import Headline, Post, Comment

#customizing representation of data on the screen
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    
@admin.register(Comment)
class CommentAdmin (admin.ModelAdmin):
    #displays properties mentioned in the tupple for each comment
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    
    #approves multiple comments at once
    actions = ['approve_comments']
    
    def approve_comments(self, request, queryset):
        queryset.update(active=True)
        

admin.site.register(Post, PostAdmin)
admin.site.register(Headline)