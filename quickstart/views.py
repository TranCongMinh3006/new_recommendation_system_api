from django.contrib.auth.models import User, Group
from . models import Article_Category, Article_Tags, Articles, Category, Tags, User_Comments, User_View, Users
from rest_framework import viewsets
from rest_framework import permissions
from quickstart.serializers import Article_CategorySerializer, Article_TagsSerializer, ArticlesSerializer, CategorySerializer, UserSerializer, GroupSerializer, TagSerializer, User_CommentSerializer, User_ViewSerializer, UsersSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
import json
from django.http import JsonResponse
from rest_framework.response import Response
import datetime


time_now = int(datetime.datetime.now().timestamp())

time_72h_before = time_now - 60 * 60 * 24 * 3

# -----------------------------------------------------------------
new_articles = Articles.objects.filter(time__gt=time_72h_before)[:200]


# -----------------------------------------------
number_of_articles = 200
hot_article_in72h = Articles.objects.filter(
    time__gt=time_72h_before)[:number_of_articles]
hot_article_in72h_id = hot_article_in72h.values_list('articleID', flat=True)
for i in list(hot_article_in72h_id):
    tmp = Articles.objects.get(pk=i)
    click_score = tmp.click_counter
    ID = tmp.articleID
    number_of_comments = User_Comments.objects.filter(
        articleID=ID).count()

    hot_score = number_of_comments*9 + click_score
    tmp.hot_score = hot_score

hot_articles = Articles.objects.all().order_by('-hot_score',)[:20]

# ------------------------------------------------


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class UsersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.IsAuthenticated]


class User_View_ViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = User_View.objects.all()
    serializer_class = User_ViewSerializer
    permission_classes = [permissions.IsAuthenticated]


class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Tags.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]


class Article_Tags_ViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Article_Tags.objects.all()
    serializer_class = Article_TagsSerializer
    permission_classes = [permissions.IsAuthenticated]


class User_Comment_ViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = User_Comments.objects.all()
    serializer_class = User_CommentSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # @action(detail=False)
    # def get_all_comment_by_id(self, request):
    #     comment_by_id = User_Comments.objects.filter(articleID = request.data.articleID)
    #     page = self.paginate_queryset(comment_by_id)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)

    #     serializer = self.get_serializer(comment_by_id, many=True)
    #     return Response(serializer.data)

    # def create(self, request):
    #     print("hello")
    #     # Now you have a clean valid email string 
    #     # You might want to call an external API or modify another table
    #     # (eg. keep track of number of accounts registered.) or even
    #     # make changes to the email format.

    #     # Once you are done, create the instance with the validated data
    #     # return models.YourModel.objects.create(email=email, **validated_data)
        # return Response("hello")


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAuthenticated]

# cai nay da ok vi no kha nhanh
    @action(detail=False)
    def get_top_level_category(self, request):
        new_article = Category.objects.filter(level=0)
        page = self.paginate_queryset(new_article)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(new_article, many=True)
        return Response(serializer.data)

# hàm lấy tất cả các bài theo category
#   đã ok nhưng thời gian chạy hơi lâu đặc biệt với các category với level cao như 0,
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        article_category = Article_Category.objects.filter(
            categoryID=instance.categoryID)[:20]
        lst = []
        for e in article_category:
            article1 = Articles.objects.get(articleID=e.articleID)
            lst.append(article1)
        lst1 = []
        for x in lst[:100]:  # trả về 100 bài báo theo category nhung chua phai la moi nhat
            dic = {
                'articleID': x.articleID,
            }
            lst1.append(dic)
        return JsonResponse(lst1, safe=False)


class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=False)
    def get_articles(self, request):
        article_id = Articles.objects.all().order_by(
            '-time',)[:100].values_list('articleID', flat=True)
        dic = {}
        dic['articleID'] = list(article_id)
        return JsonResponse(dic)


# phần này đã ok , trả về artical detail  và tagid, commentid


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        comment = User_Comments.objects.filter(
            articleID=instance.articleID).values_list('commentID', flat=True)
        tag = Article_Tags.objects.filter(
            articleID=instance.articleID).values_list('tagID', flat=True)
        dic = {
            'articleID': instance.articleID,
            'representation': instance.representation,
            'link': instance.link,
            'category': instance.category,
            'displayContent': instance.displayContent,
            'content': instance.content,
            'time': instance.time,
            'title': instance.title,
            'tags': instance.tags,
            'sapo': instance.sapo,
            'thumbnail': instance.thumbnail,
            'click_counter': instance.click_counter,
            'hot_score': instance.hot_score
        }
        dic['comments'] = list(comment)
        dic['tags'] = list(tag)
        return JsonResponse(dic)

# phần này đã ok
    @action(detail=False)
    def new_article(self, request):
        new_article = new_articles

        page = self.paginate_queryset(new_article)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(new_article, many=True)
        return Response(serializer.data)


# đã làm được nhưng thời gian quá lâu , cần cải thiện sau

    @action(detail=False)
    def hot_article(self, request):
        hot_article = hot_articles
        page = self.paginate_queryset(hot_article)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(hot_article, many=True)
        return Response(serializer.data)


class Article_CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Article_Category.objects.all()
    serializer_class = Article_CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class Article_CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Article_Category.objects.all()
    serializer_class = Article_CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
