from django.db.models import Q
from django.utils import timezone

import django_filters

from core.models import Volume
from core.query import only_current_source

from api.v2.serializers.details import VolumeSerializer
from api.v2.views.base import AuthViewSet


class VolumeFilter(django_filters.FilterSet):
    min_size = django_filters.NumberFilter(name="size", lookup_type='gte')
    max_size = django_filters.NumberFilter(name="size", lookup_type='lte')

    class Meta:
        model = Volume
        fields = ['min_size', 'max_size', 'projects']


class VolumeViewSet(AuthViewSet):
    """
    API endpoint that allows providers to be viewed or edited.
    """
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer
    filter_class = VolumeFilter
    http_method_names = ['get', 'put', 'patch', 'head', 'options', 'trace']

    def get_queryset(self):
        """
        Filter projects by current user
        """
        user = self.request.user
        now = timezone.now()
        return Volume.objects.filter(
            only_current_source(now),
            instance_source__created_by=user)
