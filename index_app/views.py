from django.http import HttpResponse, HttpRequest
from django.views import View


class Index(View):
    def get(self, request:HttpRequest) -> HttpResponse:
        return HttpResponse("<h1>hell world</h1>")
