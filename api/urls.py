from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryDestroyViewSet, CategoryListCreateViewSet,
                    CommentViewSet, GenreDestroyViewSet,
                    GenreListCreateViewSet, ReviewViewSet,
                    TitleListCreateViewSet, TitleRetrieveUpdateDestroyViewSet)

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register(
    r'titles\/(?P<title_id>\d+)\/reviews',
    ReviewViewSet,
    basename='review'
)
router_v1.register(
    r'titles\/(?P<title_id>\d+)\/reviews\/(?P<review_id>\d+)\/comments',
    CommentViewSet,
    basename='comment'
)
router_v1.register('titles', TitleListCreateViewSet, basename='titles')
router_v1.register(
    'titles',
    TitleRetrieveUpdateDestroyViewSet,
    basename='title'
)
router_v1.register(
    'categories',
    CategoryListCreateViewSet,
    basename='categories'
)
router_v1.register('categories', CategoryDestroyViewSet, basename='category')
router_v1.register('genres', GenreListCreateViewSet, basename='genres')
router_v1.register('genres', GenreDestroyViewSet, basename='genre')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
] 
