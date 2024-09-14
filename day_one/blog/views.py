from django.shortcuts import HttpResponse
from datetime import datetime


# Create your views here.

# Сделать 3 view (function based views)
# 1 - hello/ будет возвращать ответ HttResponse с текстом "Hello! Its my project"
# 2 - now_date/ будет возвращать ответ HttpResponse c нынешней датой
# 3 - goodby/ будет возвращать ответ HttpResponse с текстом “Goodby user!”


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello! Its my project')


def now_date_view(request):
    if request.method == 'GET':
        current_date = datetime.now()
        return HttpResponse(f'current date: {current_date}')


def goodby_view(request):
    if request.method == 'GET':
        return HttpResponse('Goodby user!')
