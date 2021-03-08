from django.shortcuts import render, HttpResponse
from django.views import View
import json
from hypernews.settings import NEWS_JSON_PATH

news = json.load(open(NEWS_JSON_PATH))


class MainView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Coming soon")


class NewsView(View):
    def get(self, request, news_id,  *args, **kwargs):
        for data in news:
            if data["link"] == news_id:
                return HttpResponse(f"<h2>{data['title']}</h2>"
                                    f"<p>{data['created']}</p>"
                                    f"<p>{data['text']}</p>"
                                    f'<a target="_blank" target="_blank" href="/news/">')
        return HttpResponse('')
