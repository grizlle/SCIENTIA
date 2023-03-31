from rest_framework import serializers

from publications.models import Publication
from users.models import CustomUser


class UserPublicationSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "User 1"
        model = Publication
        fields = ('id', 'title')


class UserSerializer(serializers.ModelSerializer):
    publication_list = UserPublicationSerializer(many=True, read_only=True)

    class Meta:
        ref_name = "User 1"
        model = CustomUser
        fields = ('id', 'last_name', 'first_name', 'patronymic', 'fio', 'email', 'username', 'publication_list', 'avatar_url')
