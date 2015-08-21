from rest_framework import serializers, viewsets
from rest_framework.response import Response

from nx.models import Donate


class NoteDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Donate
        fields = ("username", "phone_number", "address", "donation_type", "new", "number", "photo", "description")


class AllListView(viewsets.ModelViewSet):
    serializer_class = NoteDetailSerializer

    def list(self, request):
        queryset = Donate.objects.filter()
        serializer = NoteDetailSerializer(queryset, many=True)
        return Response(serializer.data)
