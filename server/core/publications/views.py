from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import viewsets, generics

from publications.models import Publication
from publications.serializers import (PublicationSerializer,
                                      PublicationListSerializer,
                                      PublicationDetailSerializer)
from publications.filters import PublicationFilter
from publications.serializers import FiltersInfoSerializer
from publications.filters_info import get_filters_info


class PublicationsViewSet(viewsets.ModelViewSet):
    serializer_classes = {
        'list': PublicationListSerializer,
        'retrieve': PublicationDetailSerializer,
    }
    default_serializer_class = PublicationSerializer
    queryset = Publication.objects.all().order_by('-time_create')
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PublicationFilter

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)


class FiltersInfoView(generics.GenericAPIView):
    serializer_class = FiltersInfoSerializer

    def get(self, request, *args, **kwargs):
        filters_info = get_filters_info()
        serializer = self.get_serializer(filters_info, many=True)
        return Response(serializer.data)
