from django.shortcuts import render
from django.views import View
from vacancy.models import Vacancy


class VacancyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vacancy/vacancy.html', {'vacancies': Vacancy.objects.all()})
