from django.shortcuts import render, HttpResponse
from django.views import View


class StartView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Coming soon")
