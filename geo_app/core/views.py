from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import (
    BaeaNests, BaeaSurveys, BuowlHabitat, BuowlSurveys, GbhRookeries,
    LinearProjects, RaptorNests, RaptorSurveys
)


def index(request):
    return render(request, 'index.html')

def baea_nests(request):
    data = serialize('geojson', BaeaNests.objects.all())
    return HttpResponse(data, content_type='geojson')

def baea_surveys(request):
    data = serialize('json', BaeaSurveys.objects.all())
    return HttpResponse(data, content_type='json')

def buowl_habitat(request):
    data = serialize('geojson', BuowlHabitat.objects.all())
    return HttpResponse(data, content_type='geojson')

def buowl_surveys(request):
    data = serialize('json', BuowlSurveys.objects.all())
    return HttpResponse(data, content_type='json')

def raptor_nests(request):
    data = serialize('geojson', RaptorNests.objects.all())
    return HttpResponse(data, content_type='geojson')

def raptor_surveys(request):
    data = serialize('json', RaptorSurveys.objects.all())
    return HttpResponse(data, content_type='json')

def gbh_rookeries(request):
    data = serialize('geojson', GbhRookeries.objects.all())
    return HttpResponse(data, content_type='geojson')

def linear_projects(request):
    data = serialize('geojson', LinearProjects.objects.all())
    return HttpResponse(data, content_type='geojson')