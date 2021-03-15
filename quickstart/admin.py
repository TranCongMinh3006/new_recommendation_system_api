from django.contrib import admin

# Register your models here.
from .models import Articles, Tags, Article_Category, Category, Article_Tags, User_Comments, User_View

admin.site.register(Articles)
admin.site.register(Tags)
admin.site.register(Article_Tags)
admin.site.register(Category)
admin.site.register(Article_Category)
admin.site.register(User_View)
admin.site.register(User_Comments)