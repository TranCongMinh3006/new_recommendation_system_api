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
    permission_classes = [permissions.IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=False)
    def get_top_level_category(self, request):
        new_article = Category.objects.filter(level = 0)
        page = self.paginate_queryset(new_article)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(new_article, many=True)
        return Response(serializer.data)

# hàm lấy tất cả các bài theo category
#   đã ok nhưng thời gian chạy hơi lâu đặc biệt với các category với level cao như 0, 
# hỏi thầy trả về articleid được ko , sau khi có articleid thì lại tham chiếu đến article sau
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        article_category = Article_Category.objects.filter(categoryID = instance.categoryID)
        lst =[]
        for e in article_category:
            article1 = Articles.objects.get(articleID = e.articleID)
            lst.append(article1)
        lst1=[]
        for x in lst:
            dic = {
                'articleID': x.articleID,
                'representation' : x.representation,
                'link': x.link,
                'category': x.category,
                'displayContent': x.displayContent,
                'content': x.content,
                'time': x.time,
                'title': x.title,
                'tags': x.tags,
                'sapo': x.sapo,
                'thumbnail': x.thumbnail,
                'click_counter': x.click_counter,
                'hot_score': x.hot_score
            }
            lst1.append(dic)
        return JsonResponse(lst1,safe=False)



class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Articles.objects.all().order_by('-time',)[:500]
    serializer_class = ArticlesSerializer
    permission_classes = [permissions.IsAuthenticated]

        # def list(self, request):
        # queryset = User.objects.all()
        # serializer = UserSerializer(queryset, many=True)
        # return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # article_tag = Article_Category.objects.filter(articleID = instance.articleID)
        comment = User_Comments.objects.filter(articleID = instance.articleID)

        commentlst =[]
        for e in comment:
            commentlst.append(e.content)

        dic = {
            'articleID': instance.articleID,
            'representation' : instance.representation,
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
        dic['comments'] = commentlst
        return JsonResponse(dic)

# phần này đã ok
    @action(detail=False)
    def new_article(self, request):
        new_article = Articles.objects.all().order_by('-time',)
        print(type(new_article))

        page = self.paginate_queryset(new_article)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(new_article, many=True)
        return Response(serializer.data)


# đã làm được nhưng thời gian quá lâu , cần cải thiện sau
    @action(detail=False)
    def hot_article(self, request):
        number_of_articles = Articles.objects.all().count()
        weight = 3
        for i in range(1, number_of_articles+1):
            click_score = Articles.objects.all()[i-1].click_counter
            ID = Articles.objects.all()[i-1].articleID
            number_of_comments = User_Comments.objects.filter(articleID=ID).count()


            hot_score1 = number_of_comments*weight + click_score

            Articles.objects.all()[i-1].hot_score=hot_score1

        hot_article = Articles.objects.all().order_by('-hot_score',)

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


