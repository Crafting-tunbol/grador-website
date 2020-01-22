import requests

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def homePageView(request):
    response = requests.get('http://api.syfaro.net/minecraft/1.3/server/status?ip=78.241.252.226&port=25565')
    server = response.json()
    if server['online'] and server['status'] == 'success':
        server['status'] = 'En ligne'
        server['color'] = 'green'
    else:
        server['status'] = 'Maintenance'
        server['color'] = 'red'
    return render(request, 'index.html', {'server' : server})
