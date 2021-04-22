from django.shortcuts import render, redirect
from django.views import View
from vacancy.models import Vacancy
from django.http import HttpResponseForbidden



class VacancyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vacancy/vacancy.html', {'vacancies': Vacancy.objects.all()})


class CreateVacancyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vacancy/create.html')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            Vacancy.objects.create(description=request.POST.get('description'), author=request.user)
            return redirect('http://127.0.0.1:8000/home')
        else:
            return HttpResponseForbidden()
