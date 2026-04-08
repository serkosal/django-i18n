from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

from django.utils.translation import gettext as _

# Create your views here.

def index(req: HttpRequest):
    return HttpResponse( _('index test') )