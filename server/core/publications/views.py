from django.shortcuts import render
from rest_framework import viewsets

from publications.models import Publication
from publications.serializers import PublicationSerializer


class PublicationsViewSet(viewsets.ModelViewSet):
    serializer_class = PublicationSerializer
    queryset = Publication.objects.all()
