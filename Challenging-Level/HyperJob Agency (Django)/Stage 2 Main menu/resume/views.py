from django.shortcuts import render
from django.views import View
from resume.models import Resume


class ResumeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'resume/resume.html', {'resumes': Resume.objects.all()})