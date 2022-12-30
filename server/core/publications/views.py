from django.shortcuts import render
from rest_framework import viewsets

from publications.models import Publication
from publications.serializers import PublicationSerializer, PublicationListSerializer


class PublicationsViewSet(viewsets.ModelViewSet):
    serializer_classes = {
        'list': PublicationListSerializer,
        'retrieve': PublicationListSerializer,
    }
    default_serializer_class = PublicationSerializer
    queryset = Publication.objects.all().order_by('-time_create')

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)