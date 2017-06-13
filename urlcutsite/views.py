import json

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.template.context_processors import csrf

from .models import Url


def index(request):
    return render(request, 'urlcutsite/index.html', csrf(request))
 
def redirect_original(request, short_id):
    url = get_object_or_404(Url, pk=short_id)
    url.counter += 1
    url.save()
    return HttpResponseRedirect(url.url)
 
def shorten_url(request):
    url_validator = URLValidator()
    req_url = request.POST.get("url")

    try:
        url_validator(req_url)
        url, _ = Url.objects.get_or_create(url=req_url)
        response_data = {'url': settings.SITE_URL + "/" + url.short_id}
    except ValidationError as e:
        response_data = {"error": str(e.message)}

    return HttpResponse(json.dumps(response_data),  content_type="application/json")

def show_stats(request, short_id):
    url = get_object_or_404(Url, pk=short_id)
    stats = {
        'url': url.url,
        'submitter': url.submitter.username,
        'counter': url.counter,
    }
    return render(
        request,
        'urlcutsite/stats.html',
        stats,
    )
