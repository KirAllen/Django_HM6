from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView

def hello(request):
    return HttpResponse("Hello world from function!")

class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello world from Class!")

def year_post(request, year):
    text=''
    return HttpResponse(f'posts from {year}<br>{text}')

class MonthPost(View):
    def get(self, request, year, month):
        text=''
        return HttpResponse(f'posts from {year}/{month}<br>{text}')

def post_detail(request, year, month, slug):
    post = {
        "year": year,
        "month": month,
        "slug": slug,
        "title": "TITLE TITLE TITLE",
        "content": "CONTEN CONTENT CONTENT"
    }
    return JsonResponse(post, json_dumps_params={'ensure_ascii' : False})

def my_view(request):
    context = {"name": "KIR"}
    return render(request, "app3/index.html", context)

class TemplIf(TemplateView):
    template_name = 'app3/templ_if.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Hello Wordl!'
        context['number'] = 21
        return context

def view_for(request):
    my_list = ['lemon', 'tanjerine', 'disel']
    my_dict = {
        'lemon': 'fruit',
        'Thomas': 'Little Train',
        'Tanjerine': 'Mandarin',
        'Bullet Train': 'Common Train',
    }
    context = {'my_list': my_list, 'my_dict': my_dict}
    return render(request, 'app3/templ_for.html', context)