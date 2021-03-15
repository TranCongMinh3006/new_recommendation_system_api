from django.contrib.auth.models import User, Group
from django.db.models import fields
from . models import Article_Category, Article_Tags, Articles, Category, Tags, User_Comments, User_View, Users
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ['userId', 'user_name', 'password', 'name', 'representation']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tags
        fields = ['tagID','tag']

class Article_TagsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article_Tags
        fields = ['articleID','tagID']

class User_CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User_Comments
        fields=['commentID', 'userID', 'articleID', 'content', 'time']

class User_ViewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User_View
        fields=['userID', 'articleID', 'time']

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields=['categoryID', 'category', 'level']

class Article_CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article_Category
        fields = ['articleID','categoryID']

class ArticlesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Articles
        fields = ['articleID', 'representation', 'link', 'category', 'displayContent', 'content', 'title', 'tags', 'sapo']
