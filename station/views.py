from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
import requests

station_url="https://gbfs.divvybikes.com/gbfs/en/station_status.json"


def total_station_active(request):
    r=requests.get(url=station_url)
    data=r.json()
    stations= (data['data']['stations'])
    count=0
    l= len(stations)
    for station in stations:
        if station['station_status'] == "active":
            count+=1
    msg=f"total active stations are: {count}"
    return JsonResponse(msg,safe=False)
    
def total_docks_avl(request,id):
    r=requests.get(url=station_url)
    data=r.json()
    stations= (data['data']['stations'])
    l= len(stations)
    result=None
    for station in stations:
        if station['station_id'] == id:
            result=station['num_docks_available']
    msg=f"total number of available doc in station id {id} are {result}"
    return JsonResponse(msg,safe= False)

def available_bikes(request, id):
    r=requests.get(url=station_url)
    data=r.json()
    stations= (data['data']['stations'])
    result=None
    for station in stations:
        if station['station_id'] == id:
            result=station['num_bikes_available']
    msg=f"total number of available bikes in station id {id} are {result}"
    return JsonResponse(msg,safe= False)



