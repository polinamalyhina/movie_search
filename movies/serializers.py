from rest_framework import serializers


class MovieDTOSerializer(serializers.Serializer):
    id = serializers.CharField()
    title = serializers.CharField()
