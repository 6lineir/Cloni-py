from django.shortcuts import render
import requests
from django.http import HttpResponse

# Create your views here.
def getdata(request):
    api_url = "https://api.coindesk.com/v1/bpi/currentprice/IRR.json"
    price = requests.get(api_url).json()['bpi']['USD']['rate']
    time = requests.get(api_url).json()['time']['updated']
    return HttpResponse(time +' |-| '+ price)