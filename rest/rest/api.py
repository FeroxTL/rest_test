from rest.models import TestModel
from rest_framework import generics, serializers


class TestSerializer(serializers.Serializer):
    value = serializers.IntegerField()


class TestView(generics.CreateAPIView):
    serializer_class = TestSerializer

    def get_queryset(self):
        return TestModel.objects.all()
