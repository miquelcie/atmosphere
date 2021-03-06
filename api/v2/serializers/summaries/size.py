from core.models import Size
from rest_framework import serializers


class SizeSummarySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Size
        view_name = 'api:v2:size-detail'
        fields = ('id', 'url', 'alias', 'name', 'cpu', 'disk', 'mem', 'active', 'start_date', 'end_date')
