from django.urls import include, path
from rest_framework import routers
from quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'users_crawl', views.UsersViewSet)
router.register(r'user_view', views.User_View_ViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'user_comment', views.User_Comment_ViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'articles', views.ArticleViewSet)
router.register(r'article_tags', views.Article_Tags_ViewSet)
router.register(r'article_category', views.Article_CategoryViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]