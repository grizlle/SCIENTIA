from abc import ABC

from rest_framework import serializers

from publications.models import Publication
from users.models import CustomUser


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'


class PublicationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'fio', 'avatar_url')


class PublicationListSerializer(serializers.ModelSerializer):
    authors = PublicationUserSerializer(read_only=True, many=True)
    cat = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Publication
        fields = ('id', 'authors', 'title', 'publication_year', 'cat')


class PublicationDetailSerializer(serializers.ModelSerializer):
    authors = PublicationUserSerializer(read_only=True, many=True)
    cat = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Publication
        fields = '__all__'


class FiltersInfoSerializer(serializers.Serializer):
    filter_name = serializers.CharField()
    filter_type = serializers.CharField()
    filter_client_name = serializers.CharField()