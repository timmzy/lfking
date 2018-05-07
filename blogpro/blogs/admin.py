from django.contrib import admin

from blogs.models import Banner,Post,BlogCategory, Tags, FriendlyLink

admin.site.register(Banner)
# admin.site.register(Post)
admin.site.register(BlogCategory)
admin.site.register(Tags)
admin.site.register(FriendlyLink)


class PostAdmin(admin.ModelAdmin):
    class Media:
        js = (
            '/static/js/editor/kindeditor-all.js',
            '/static/js/editor/config.js',
            '/static/js/editor/lang/zh_CN.js',
        )
admin.site.register(Post, PostAdmin)