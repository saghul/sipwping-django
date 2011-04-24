
import httplib2
import socket

from django.conf import settings
from django.utils import simplejson


class OptionsRequestError(Exception): pass

class OptionsRequest(object):

    @classmethod
    def get(cls, uri):
        try:
            data = simplejson.dumps({'target_uri': uri})
            h = httplib2.Http(timeout=10)
            response, content = h.request(settings.SIPWPING_SERVER_URL, 'POST', data, headers={'Content-Type': 'application/json'})
            return content
        except (httplib2.HttpLib2Error, socket.error), e:
            raise OptionsRequestError(e)

