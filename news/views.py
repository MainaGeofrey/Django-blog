from django.shortcuts import render
from newsapi import NewsApiClient


def index (request):
    newsapi = NewsApiClient(api_key='2e2014145ca74adaa8c805b2dd46f98a')
    top = newsapi.get_top_headlines(sources='techcrunch')
    
    newsList = top['articles']
    description = []
    news = []
    image = []
    
    for i in range(len(newsList)):
        f = newsList[i]
        news.append(f['title'])
        description.append(f['description'])
        image.append(f['urlToImage'])
        
    mylist = zip(news, description, image)
    
    return render(request, 'mynews.html', {'mylist': mylist})
        