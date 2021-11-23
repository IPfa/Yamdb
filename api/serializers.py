from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from reviews.models import Catergory, Comment, Genre, Review, Title
from reviews.validators import (UNIQUE_REVIEW_VALIDATION_MESSAGE,
                                score_validation, year_validation)

# с другим расположением импортов нас не пускают на сдачу тесты Практикума


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')
    pub_date = serializers.DateTimeField(read_only=True,
                                         format='%Y-%m-%dT%H:%M:%SZ')
    text = serializers.CharField()
    score = serializers.IntegerField(validators=(score_validation,))

    class Meta:
        model = Review
        exclude = ('title', )
        read_only_fields = ('title', )

    def create(self, validated_data):
        title = validated_data.get('title')
        user = self.context.get('request').user
        if len(Review.objects.filter(author=user, title=title)) != 0:
            raise ValidationError(detail=UNIQUE_REVIEW_VALIDATION_MESSAGE)
        return Review.objects.create(**validated_data)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')
    text = serializers.CharField()
    pub_date = serializers.DateTimeField(read_only=True,
                                         format='%Y-%m-%dT%H:%M:%SZ')

    class Meta:
        model = Comment
        exclude = ('review', )
        read_only_fields = ('post', )


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'slug')
        model = Genre


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'slug')
        model = Catergory


class TitleSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    category = CategorySerializer()
    rating = serializers.SerializerMethodField(read_only=True)

    class Meta:
        fields = (
            'id',
            'name',
            'year',
            'rating',
            'description',
            'genre',
            'category'
        )
        model = Title

    def get_rating(self, obj):
        if not obj.reviews.exists():
            return None
        rewiews = obj.reviews.all()
        return sum([review.score for review in rewiews]) / len(rewiews)


class TitleCreateUpdateSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True
    )
    category = serializers.SlugRelatedField(
        queryset=Catergory.objects.all(),
        slug_field='slug'
    )
    year = serializers.IntegerField(validators=(year_validation,))

    class Meta:
        fields = ('id', 'name', 'year', 'description', 'genre', 'category')
        model = Title
