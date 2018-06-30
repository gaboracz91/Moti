from rest_framework import serializers

from service.models import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
