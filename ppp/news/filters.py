from django_filters import FilterSet
from .models import Article

# создаём фильтр
class ArticleFilter(FilterSet):
    class Meta:
        model = Article
        fields = {'title': ['icontains'],
                  'description': ['icontains'],
                  'datetime': ['gt']}
