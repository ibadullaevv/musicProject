from django.shortcuts import render
import requests



from news.models import Article

API_KEY = '9e838976d1824109835e74a03d57477e'





def news(request):
    # country = request.GET.get('country')
    # category = request.GET.get('category')
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'
    resspone = requests.get(url)
    data = resspone.json()
    articles = data['articles']
    context = {
        'articles': articles
    }
    return render(request, 'news.html', context)


def add_news():
    # country = request.GET.get('country')
    # category = request.GET.get('category')
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'
    resspone = requests.get(url)
    data = resspone.json()
    articles = data['articles']
    print(articles)
    for article in articles:
        # if not Article.objects.filter(author=article['author'], title=article['title']):
        Article.objects.create(author=article['author'], title=article['title'], description=article['description'],
                               urlToImage=article['urlToImage'])
        print('saved')
        # else:
        #     print('already exist')

    # context = {
    #     'articles': articles
    # }
    # return render(request, 'news.html', context)
