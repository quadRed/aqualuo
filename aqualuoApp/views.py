from django.shortcuts import render

import json, copy
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_POST
def plantWebhook(request):
    humidity = request.POST.get('humidity')
    temperature = request.POST.get('temperature')

    return HttpResponse(status=200,content="Values received")