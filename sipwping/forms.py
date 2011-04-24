
from django.forms import Form, RegexField


# Naive validation of a SIP URI
_sip_uri_regex = r'^((?P<user>[a-zA-Z0-9 _\-\+\.\%]+)@)?(?P<host>([a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})$'

class SIPURIForm(Form):
    uri = RegexField(label='', regex=_sip_uri_regex, error_messages={'invalid': 'Invalid SIP URI'})

