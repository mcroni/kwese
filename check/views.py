from django.shortcuts import render,HttpResponse
import requests
from django.http import JsonResponse
import json
import time
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


# def index2(request):
#     if request.method == "POST":
#         headers = {'user-agent': 'my-app/0.0.1'}
#         payload = {
#             'client_id':client_id,
#             'client_secret':client_secret
#         }
#         url = "https://graph.facebook.com/?id=https://win.kwese.com/ivy-barley.php"
#         r = requests.get(url,headers,data=json.dumps(payload))
#         print(r.text)
#         actual = json.loads(r.text)
#         actual = actual['share']['share_count']
#         data = {}
#         data['votes'] = actual
#         # time.sleep(5)
#         return JsonResponse(data)
#     return render(request,'check/index.html',{})


headers = {'user-agent': 'my-app/0.0.1'}

def index(request):
    if request.method == "POST":
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
            vote['name'] = name
            vote['votes'] = votes
            data['{0}'.format(name)] = name
            data['{0}'.format(name)] = vote
        print(data)
        return JsonResponse(data)
    return render(request,'check/index.html',{})


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
        vote['name'] = name
        vote['votes'] = votes
        data['{0}'.format(name)] = name
        data['{0}'.format(name)] = vote
    print(data)
    return JsonResponse(data)



