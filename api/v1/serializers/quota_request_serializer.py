from core.models import IdentityMembership, Quota
from core.models.request import QuotaRequest
from core.models.status_type import StatusType
from core.models.user import AtmosphereUser
from rest_framework import serializers


class QuotaRequestSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True, source="uuid", required=False)
    created_by = serializers.SlugRelatedField(
        slug_field='username',
        queryset=AtmosphereUser.objects.all())
    status = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name')
    membership = serializers.PrimaryKeyRelatedField(
        queryset=IdentityMembership.objects.all())

    provider = serializers.CharField(read_only=True, source="membership__provider__location")

    class Meta:
        model = QuotaRequest
        exclude = ('uuid',)


class ResolveQuotaRequestSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True, source="uuid", required=False)

    status = serializers.SlugRelatedField(
        slug_field='name',
        queryset=StatusType.objects.all())

    created_by = serializers.SlugRelatedField(
        slug_field='username',
        queryset=AtmosphereUser.objects.all())

    quota = serializers.SlugRelatedField(
        slug_field='id',
        queryset=Quota.objects.all())

    class Meta:
        model = QuotaRequest
        exclude = ('uuid', 'membership')


class UserQuotaRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuotaRequest
        fields = ("request", "description",)
