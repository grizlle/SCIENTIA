from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from users.models import CustomUser
from users.serializers import UserSerializer


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):

    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
