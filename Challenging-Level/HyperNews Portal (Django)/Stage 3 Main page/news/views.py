from django.shortcuts import render, HttpResponse
from django.views import View
import json
from hypernews.settings import NEWS_JSON_PATH
from collections import defaultdict
from copy import deepcopy

news = json.load(open(NEWS_JSON_PATH))


class MainView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Coming soon <h2>Hyper news</h2>")


class AllNewsView(View):
    def get(self, request, *args, **kwargs):
        prepared_news = deepcopy(sorted(news, key=lambda x: x['created'],  reverse=True))
        for dictionary in prepared_news:
            dictionary['created'] = dictionary['created'].split()[0]
        context = {'news': prepared_news}
        return render(request, r"news\newsbase.html", context=context)


class NewsView(View):
    def get(self, request, news_id,  *args, **kwargs):
        for data in news:
            if data["link"] == news_id:
                return HttpResponse(f"<h2>{data['title']}</h2>"
                                    f"<p>{data['created']}</p>"
                                    f"<p>{data['text']}</p>"
                                    f'<a href="/news/">')
        return HttpResponse('')
