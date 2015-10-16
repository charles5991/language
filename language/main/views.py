from django.shortcuts import render
import datetime


def main(request):
    now = datetime.datetime.now()
    context = {'message':'Django 很棒','time':now}
    return render(request, 'main/main.html', context)