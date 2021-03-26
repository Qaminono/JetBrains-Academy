from django.shortcuts import render, HttpResponse, redirect
from django.views import View
import json
from hypernews.settings import NEWS_JSON_PATH
from collections import defaultdict
from copy import deepcopy
from datetime import datetime

news = json.load(open(NEWS_JSON_PATH))


class MainView(View):
    def get(self, request, *args, **kwargs):
        return redirect(f'/news/')



class CreateNewsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'news/createbase.html')

    def post(self, request, *args, **kwargs):
        global news
        create_news = {'created': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                       'text': request.POST.get('text'),
                       'title': request.POST.get('title'),
                       'link': max([x['link'] for x in news]) + 1}
        news.append(create_news)
        json.dump(news, open(NEWS_JSON_PATH, 'w'))
        news = json.load(open(NEWS_JSON_PATH))
        return redirect(f'/news/')


class AllNewsView(View):
    def get(self, request, *args, **kwargs):
        q = request.GET.get('q')
        if q:
            prepared_news = [article for article in news if q.lower() in article['title'].lower()]
        else:
            prepared_news = deepcopy(sorted(news, key=lambda x: x['created'],  reverse=True))
        for dictionary in prepared_news:
            dictionary['created'] = dictionary['created'].split()[0]
        context = {'news': prepared_news}
        return render(request, "news/newsbase.html", context=context)


class NewsView(View):
    def get(self, request, news_id,  *args, **kwargs):
        if news_id:
            for article in news:
                if news_id == article['link']:
                    return render(request, "news/base.html", context=article)
        return redirect(f'/news/')
