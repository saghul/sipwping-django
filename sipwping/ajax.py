
from django.utils import simplejson
from dajaxice.core import dajaxice_functions

from sipwping.forms import SIPURIForm
from sipwping.models import OptionsRequest, OptionsRequestError


def dajaxice_function(f):
    dajaxice_functions.register(f)
    return f

@dajaxice_function
def ajax_form(request, form):
    f = SIPURIForm(form)
    response = {}
    if f.is_valid():
        data = f.cleaned_data
        try:
            data = OptionsRequest.get(data['uri'])
        except OptionsRequestError, e:
            response['error'] = str(e)
        else:
            response['status'] = simplejson.loads(data)
    else:
        response['error'] = '; '.join((', '.join(value) for value in f.errors.values()))
    return simplejson.dumps(response)


