from django.contrib.auth.models import AnonymousUser
from core.models.application import ApplicationBookmark
from rest_framework import serializers


class AppBookmarkField(serializers.Field):

    def to_representation(self, bookmark_mgr):
        request = self.context.get('request', None)
        request_user = request.user
        if type(request_user) == AnonymousUser:
            return False
        try:
            bookmark_mgr.get(user=request_user)
            return True
        except ApplicationBookmark.DoesNotExist:
            return False

    def to_internal_value(self, data, files, field_name, into):
        value = data.get(field_name)
        if value is None:
            return
        app = self.root.object
        request = self.context.get('request', None)
        user = request.user

        if value:
            ApplicationBookmark.objects.\
                get_or_create(application=app, user=user)
            result = True
        else:
            ApplicationBookmark.objects\
                               .filter(application=app, user=user).delete()
            result = False
        into[field_name] = result
