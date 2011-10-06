from django.http import HttpResponse
from django.http import HttpResponseRedirect

import urllib2 as urllib
import simplejson as json
import urlparse

FB_APP_ID = '40800285147'
FB_APP_SECRET = 'a919a96bd97e79ef208ec610d3aca38a'
REDIRECT_URI = 'http%3A%2F%2Flocalhost%3A8000%2Ffb'

def index(request):
    if request.user.is_authenticated():
	return HttpResponse("You are " + request.user.username)
    return HttpResponse("hello world!")
