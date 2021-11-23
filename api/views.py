from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from reviews.models import Catergory, Genre, Review, Title

from .filters import TitleFilter
from .mixins import ListCreateViewSet
from .permissions import AdminOrReadOnly, AuthorModerAdminOrReadOnly
from .serializers import (CategorySerializer, CommentSerializer,
                          GenreSerializer, ReviewSerializer,
                          TitleCreateUpdateSerializer, TitleSerializer)

# с другим расположением импортов нас не пускают на сдачу тесты Практикума


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (AuthorModerAdminOrReadOnly, )

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        serializer.save(author=self.request.user,
                        title=get_object_or_404(Title, id=title_id))

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        return Review.objects.filter(title=title_id)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthorModerAdminOrReadOnly, )

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        review_id = self.kwargs.get('review_id')
        get_object_or_404(Title, id=title_id)
        serializer.save(author=self.request.user,
                        review=get_object_or_404(Review, id=review_id),)

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        review_id = self.kwargs.get('review_id')
        get_object_or_404(Title, id=title_id)
        return get_object_or_404(Review, id=review_id).comments.all()


class TitleListCreateViewSet(ListCreateViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter
    permission_classes = (AdminOrReadOnly,)

    def get_serializer_class(self):
        if self.action == 'create':
            return TitleCreateUpdateSerializer
        return TitleSerializer

    def create(self, request):
        serializer = TitleCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            queryset_after_creation = Title.objects.all()
            name_after_creation = serializer.data['name']
            title_after_creation = get_object_or_404(
                queryset_after_creation,
                name=name_after_creation
            )
            serializer_after_creation = TitleSerializer(title_after_creation)
            return Response(
                serializer_after_creation.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class TitleRetrieveUpdateDestroyViewSet(viewsets.ViewSet):
    permission_classes = (AdminOrReadOnly,)

    def retrieve(self, request, pk=None):
        queryset = Title.objects.all()
        title = get_object_or_404(queryset, pk=pk)
        serializer = TitleSerializer(title)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        queryset = Title.objects.all()
        title = get_object_or_404(queryset, pk=pk)
        serializer = TitleCreateUpdateSerializer(
            title,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
        queryset_after_update = Title.objects.all()
        title_after_update = get_object_or_404(queryset_after_update, pk=pk)
        serializer_after_update = TitleSerializer(title_after_update)
        return Response(serializer_after_update.data)

    def destroy(self, request, pk=None):
        queryset = Title.objects.all()
        title = get_object_or_404(queryset, pk=pk)
        title.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryListCreateViewSet(ListCreateViewSet):
    queryset = Catergory.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    permission_classes = (AdminOrReadOnly,)


class CategoryDestroyViewSet(viewsets.ViewSet):
    permission_classes = (AdminOrReadOnly,)

    def destroy(self, request, pk=None):
        queryset = Catergory.objects.all()
        category = get_object_or_404(queryset, slug=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GenreListCreateViewSet(ListCreateViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = PageNumberPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    permission_classes = (AdminOrReadOnly,)


class GenreDestroyViewSet(viewsets.ViewSet):
    permission_classes = (AdminOrReadOnly,)

    def destroy(self, request, pk=None):
        queryset = Genre.objects.all()
        category = get_object_or_404(queryset, slug=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
