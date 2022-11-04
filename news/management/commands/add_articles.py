import requests
from django.core.management.base import BaseCommand

from news.models import Article

API_KEY = '9e838976d1824109835e74a03d57477e'


class Command(BaseCommand):
    help = 'Adding article from internet'

    def add_arguments(self, parser):
        parser.add_argument('quantity', type=int, nargs='?', default=1)

    def handle(self, *args, **options):

        quantity = options.get('quantity')
        url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
        resspone = requests.get(url)
        data = resspone.json()
        article_count = data['totalResults']
        articles = data['articles']
        if quantity > article_count:
            raise Exception(f'Siz artikllar soni {article_count} dan ko\'p kiritdingiz')
        for article in articles[:quantity]:
            if not Article.objects.filter(description=article['description'], title=article['title']).exists():
                Article.objects.create(author=article['author'], title=article['title'],
                                       description=article['description'],
                                       urlToImage=article['urlToImage'])
            print(article['author'])
