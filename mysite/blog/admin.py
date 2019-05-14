from django.contrib import admin

# Register your models here.
from blog.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')   # 显示列表的内容
    list_filter = ('status', 'created', 'publish', 'author')    # 列表过滤器
    search_fields = ('title', 'body')                           # 搜索框的范围
    prepopulated_fields = {'slug': ('title',)}                  # 预先填写内容。这里指slug列将根据title列的内容填写
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'                                  # 日期层次等级
    ordering = ('status', 'publish')                            # 排序


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
