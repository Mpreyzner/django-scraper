from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from collections import Counter
import json
from ..stats.serializers import AuthorStatsSerializer, TotalStatsSerializer
from ..stats.models import AuthorStats, TotalStats
from ..scraper.serializers import AuthorSerializer
from ..scraper.models import Author


# TODO move serialization back to serializers

class AuthorList(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        authors = {}
        for author in queryset.all():
            authors.update({author.tokenized_name: author.name})
        return Response(authors)


@api_view(http_method_names=['GET'])
def author_stats(request, author):
    # TODO make this a class
    author = Author.objects.get(tokenized_name=author)
    stats = AuthorStats.objects.get(author=author)
    counter = Counter(json.loads(stats.word_counts))
    return Response(dict(counter.most_common(10)))


class TotalStats(generics.ListAPIView):
    queryset = TotalStats.objects.all()
    serializer_class = TotalStatsSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        stats = queryset.first()
        counter = Counter(json.loads(stats.word_counts))
        return Response(dict(counter.most_common(10)))
