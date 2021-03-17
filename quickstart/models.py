from django.db import connections
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Articles(models.Model):
    articleID = models.IntegerField(primary_key=True)
    representation = models.TextField()
    link = models.TextField()
    category = models.TextField()
    displayContent = models.TextField()
    content = models.TextField()
    title = models.CharField(max_length=255)
    tags = models.TextField()
    sapo = models.TextField()
    class Meta:
        db_table = "articles"


class Tags(models.Model):   
    tagID = models.IntegerField(primary_key=True)
    tag = models.TextField()
    class Meta:
        db_table = "tags"

# class Article_Tags(models.Model):   
#     articleID = models.IntegerField()
#     tagID = models.IntegerField()
#     class Meta:
#         db_table = "article_tags"

class Article_Tags(models.Model):
    id = models.IntegerField(primary_key=True)
    articleID = models.ForeignKey(Articles, on_delete=models.CASCADE)
    tagID = models.ForeignKey(Tags, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("articleID", "tagID"),)
        db_table = "article_tags"


class Category(models.Model):   
    categoryID = models.IntegerField(primary_key=True)
    category = models.TextField()
    level = models.IntegerField()
    class Meta:
        db_table = "category"

class Article_Category(models.Model):   
    articleID = models.IntegerField()
    categoryID = models.IntegerField()
    class Meta:
        db_table = "article_category"

class User_Comments(models.Model):   
    commentID = models.IntegerField(primary_key=True)
    # userID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    articleID = models.ForeignKey(Articles, on_delete=models.CASCADE)
    content = models.TextField()
    time = models.IntegerField()
    class Meta:
        db_table = "user_comments"


class Users(models.Model):   # this model is crawled users from vnexpress
    userId = models.IntegerField(primary_key=True)
    user_name = models.TextField()
    password = models.TextField()
    name = models.TextField()
    representation = models.TextField()
    class Meta:
        db_table = "users"

class User_View(models.Model):   
    userID = models.IntegerField()
    articleID = models.IntegerField()
    time = models.IntegerField()
    class Meta:
        db_table = "user_view"