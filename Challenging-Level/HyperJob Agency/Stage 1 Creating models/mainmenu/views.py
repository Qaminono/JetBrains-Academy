from django.http.response import HttpResponse
from django.views import View




class MainMenuView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h2>Welcome to HyperJob!</h2>'
                            '<div> <a href="/login">Login page</div>'
                            '<div> <a href="/signup">Sign up page</div>'
                            '<div> <a href="/vacancies">Vacancy list</div>'
                            '<div> <a href="/resumes">Resume list</div>'
                            '<div> <a href="/home">Personal profile</div>'
                            '<audio controls src="https://s3.amazonaws.com/pb_previews/387_snappy/387_full_snappy_0151_preview.mp3"></audio>')
