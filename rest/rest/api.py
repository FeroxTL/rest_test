from rest.models import TestModel
from rest_framework import generics, serializers


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = ['value']


class TestView(generics.CreateAPIView):
    serializer_class = TestSerializer

    def get_queryset(self):
        return TestModel.objects.all()
