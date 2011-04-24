
from django.utils import simplejson

from sipwping.forms import SIPURIForm
from sipwping.models import OptionsRequest, OptionsRequestError
from sipwping.util import render_response


def index(request):
    if request.method == 'POST':
        form = SIPURIForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            data = form.cleaned_data
            try:
                data = OptionsRequest.get(data['uri'])
            except OptionsRequestError, e:
                context['error'] = e
            else:
                context['status'] = simplejson.loads(data)
        else:
            context['error'] = '; '.join((', '.join(value) for value in form.errors.values()))
    else:
        form = SIPURIForm()
        context = {'form': form}
    return render_response(request, 'sipwping/index.html', context)

