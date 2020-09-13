from django.contrib import admin
from blog.models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin


admin.site.site_header = 'Infix Studios Admin'

class PostAdmin2(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on',)
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class PostAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    summernote_fields = ('content',)
    list_display = ('title', 'slug', 'status','created_on',)
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)