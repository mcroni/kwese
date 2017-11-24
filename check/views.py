from django.shortcuts import render,HttpResponse
import requests
from django.http import JsonResponse
import json
from .models import Contestant
client_secret = '86dec6262eab31210b626b032dad0817'
client_id = '229203697589598'

links = ['https://graph.facebook.com/?id=https://win.kwese.com/ivy-barley.php',
         'https://graph.facebook.com/?id=https://win.kwese.com/abisola-akindeinde.php',
         'https://graph.facebook.com/?id=https://win.kwese.com/dumisani-mahlangu.php',
         'https://graph.facebook.com/?id=https://win.kwese.com/sarah-uwitonze.php',
         'https://graph.facebook.com/?id=https://win.kwese.com/shola-peter.php',
         'https://graph.facebook.com/?id=https://win.kwese.com/veridique-musambaghani-kakule.php',
         'https://graph.facebook.com/?id=https://win.kwese.com/bankole-olalekan.php',
         'https://graph.facebook.com/?id=https://win.kwese.com/pascal-akahome.php',
         'https://graph.facebook.com/?id=https://win.kwese.com/ezinne-uko.php',
         'https://graph.facebook.com/?id=https://win.kwese.com/blessing-machiya.php',
         'https://graph.facebook.com/?id=https://win.kwese.com/peter-wachira.php',
         'https://graph.facebook.com/?id=https://win.kwese.com/farai-nechikwira.php']

proxies = {'https': 'http://180.247.12.6:8080'}

headers = {'user-agent': 'my-app/0.0.1'}

def index(request):
    pascal = Contestant.objects.get(name='Pascal Akahome').votes
    dum = Contestant.objects.get(name='Dumisani Mahlangu').votes
    bank = Contestant.objects.get(name='Olalekan Bankole Emmanuel').votes
    ver = Contestant.objects.get(name='Veridique Musambaghani Kakule').votes
    shola = Contestant.objects.get(name='Shola Peter').votes
    sarah = Contestant.objects.get(name='Uwitonze Sarah').votes
    abisola = Contestant.objects.get(name='Abisola Akindeinde').votes
    ivy = Contestant.objects.get(name='Ivy Barley').votes
    ezin = Contestant.objects.get(name='Ezinne Uko').votes
    blessing = Contestant.objects.get(name='Blessing Machiya').votes
    farai = Contestant.objects.get(name='Farai Nechikwira').votes
    peter = Contestant.objects.get(name='Peter Wachira').votes

    context = {
        'pascal' : pascal,
        'ivy': ivy,
        'peter': peter,
        'farai': farai,
        'blessing': blessing,
        'ezin': ezin,
        'abisola': abisola,
        'sarah': sarah,
        'shola': shola,
        'ver': ver,
        'bank': bank,
        'dum': dum,

    }
    return render(request,'check/index.html',context)


def getter(request):
    headers = {'user-agent': 'my-app/0.0.1'}
    payload = {
        'client_id': client_id,
        'client_secret': client_secret
    }
    data = {}
    for url in links:
        r = requests.get(url, headers=headers,data=json.dumps(payload))
        actual = json.loads(r.text)
        print(actual)
        name = actual['og_object']['title']
        votes = actual['share']['share_count']
        vote = {}
        Contestant.objects.filter(name=name).update(votes=votes)
        vote['name'] = name
        vote['votes'] = votes
        data['{0}'.format(name)] = name
        data['{0}'.format(name)] = vote
    print(data)
    return JsonResponse(data)



