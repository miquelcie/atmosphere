from rest_framework.decorators import detail_route

from core.models import Project, Group
from core.query import only_current

from api.v2.serializers.details import ProjectSerializer,\
    VolumeSerializer, InstanceSerializer
from api.v2.views.base import AuthViewSet


class ProjectViewSet(AuthViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        user = self.request.user
        group = Group.objects.get(name=user.username)
        serializer.save(owner=group)

    def get_queryset(self):
        """
        Filter projects by current user.
        """
        user = self.request.user
        return Project.objects.filter(only_current(),
                                      owner__name=user.username)

    @detail_route()
    def instances(self, *args, **kwargs):
        project = self.get_object()
        self.get_queryset = super(AuthViewSet, self).get_queryset
        self.queryset = project.instances.get_queryset()
        self.serializer_class = InstanceSerializer
        return self.list(self, *args, **kwargs)

    @detail_route()
    def volumes(self, *args, **kwargs):
        project = self.get_object()
        self.get_queryset = super(AuthViewSet, self).get_queryset
        self.queryset = project.volumes.get_queryset()
        self.serializer_class = VolumeSerializer
        return self.list(self, *args, **kwargs)
