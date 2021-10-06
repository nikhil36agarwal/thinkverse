from django.shortcuts import render
import requests
import json
from newsapi import NewsApiClient


# Create your views here.

from django.http import HttpResponse, response

def home(request):
    newsapi = NewsApiClient(api_key='5dd3a0be41aa417386f6c3bbe8526b67')
# /v2/top-headlines
    top = newsapi.get_top_headlines(country='us')
    l = top['articles']
    urlink = []
    img =[]
  
    for i in range(len(top['articles'])):
        f = l[i]
        img.append(f['urlToImage'])
        urlink.append(f['url'])
    
    mylist = zip(img, urlink)

    print(len(l))

    return render(request, 'mysite/home.html', context ={"mylist":mylist})




def page2(request):
    newsapi = NewsApiClient(api_key='5dd3a0be41aa417386f6c3bbe8526b67')
# /v2/top-headlines
    top = newsapi.get_top_headlines(sources = 'bbc-news')
    l = top['articles']
    urlink = []
    img =[]
  
    for i in range(len(top['articles'])):
        f = l[i]
        img.append(f['urlToImage'])
        urlink.append(f['url'])
    
    mylist = zip(img, urlink)
    return render(request, 'mysite/page2.html', context = {"mylist":mylist})  




def page3(request):
    newsapi = NewsApiClient(api_key='5dd3a0be41aa417386f6c3bbe8526b67')
# /v2/top-headlines
    top = newsapi.get_top_headlines(country = 'de', category = 'business')
    l = top['articles']
    urlink = []
    img =[]
  
    for i in range(len(top['articles'])):
        f = l[i]
        img.append(f['urlToImage'])
        urlink.append(f['url'])
    
    mylist = zip(img, urlink)
    print(len(l))
    return render(request, 'mysite/page3.html', context = {"mylist":mylist}) 




def page4(request):
    newsapi = NewsApiClient(api_key='5dd3a0be41aa417386f6c3bbe8526b67')
# /v2/top-headlines
    top = newsapi.get_top_headlines(q = 'trump')
    l = top['articles']
    urlink = []
    img =[]
  
    for i in range(len(top['articles'])):
        f = l[i]
        img.append(f['urlToImage'])
        urlink.append(f['url'])
    
    mylist = zip(img, urlink)

    return render(request, 'mysite/page4.html', context = {"mylist":mylist}) 