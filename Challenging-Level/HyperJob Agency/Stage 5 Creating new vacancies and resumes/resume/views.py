from django.shortcuts import render, redirect
from django.views import View
from resume.models import Resume
from django.http import HttpResponseForbidden


class ResumeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'resume/resume.html', {'resumes': Resume.objects.all()})


class CreateResumeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'resume/create.html')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and not request.user.is_staff:
            Resume.objects.create(description=request.POST.get('description'), author=request.user)
            return redirect('http://127.0.0.1:8000/home')
        else:
            return HttpResponseForbidden()
