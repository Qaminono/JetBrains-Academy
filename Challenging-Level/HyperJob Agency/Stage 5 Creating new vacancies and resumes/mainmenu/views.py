from django.http.response import HttpResponse
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView
from django.shortcuts import render


class MainMenuView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h2>Welcome to HyperJob!</h2>'
                            '<div> <a href="/login">Login page</div>'
                            '<div> <a href="/signup">Sign up page</div>'
                            '<div> <a href="/vacancies">Vacancy list</div>'
                            '<div> <a href="/resumes">Resume list</div>'
                            '<div> <a href="/home">Personal profile</div>')


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = '/login'
    template_name = 'signup.html'


class MyLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = 'login.html'


class HomeView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                return render(request, 'new_vacancy.html')
        return render(request, 'new_resume.html')
