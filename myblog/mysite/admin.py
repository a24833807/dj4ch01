from django.contrib import admin # type: ignore
from mysite.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')

admin.site.register(Post,PostAdmin)