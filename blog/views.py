from django.shortcuts import render
from django.http.request import HttpRequest

from django.utils.translation import gettext as _

# Create your views here.

def index(req: HttpRequest):
    
    context = {
        'title': _('Main page')
    }
    
    return render(req, 'django_proj/base.html', context=context)