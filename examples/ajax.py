import random

from django.utils import simplejson
from django.template.loader import render_to_string

from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form
from dajax.core import Dajax

from forms import ExampleForm
from views import get_pagination_page


@dajaxice_register
def dajaxice_example(request):
    return simplejson.dumps({'message': 'Hello from Python!'})


@dajaxice_register
def args_example(request, text):
    return simplejson.dumps({'message': 'Your message is %s!' % text})


@dajaxice_register
def multiply(request, a, b):
    dajax = Dajax()
    result = int(a) * int(b)
    dajax.assign('#result', 'value', str(result))
    return dajax.json()


@dajaxice_register
def randomize(request):
    dajax = Dajax()
    dajax.assign('#result', 'value', random.randint(1, 10))
    return dajax.json()


@dajaxice_register
def updatecombo(request, option):
    dajax = Dajax()
    options = [['Madrid', 'Barcelona', 'Vitoria', 'Burgos'],
               ['Paris', 'Evreux', 'Le Havre', 'Reims'],
               ['London', 'Birmingham', 'Bristol', 'Cardiff'], ]
    out = []

    for option in options[int(option)]:
        out.append("<option value='#'>%s</option>" % option)

    dajax.assign('#combo2', 'innerHTML', ''.join(out))
    return dajax.json()


@dajaxice_register
def send_form(request, form):
    dajax = Dajax()
    form = ExampleForm(deserialize_form(form))

    if form.is_valid():
        dajax.remove_css_class('#my_form input', 'error')
        dajax.alert("Form is_valid(), your username is: %s" % form.cleaned_data.get('username'))
    else:
        dajax.remove_css_class('#my_form input', 'error')
        for error in form.errors:
            dajax.add_css_class('#id_%s' % error, 'error')

    return dajax.json()


@dajaxice_register
def request_points(request):
    dajax = Dajax()
    points = [
        {'lat':37.41444798751896, 'lng':-122.0916223526001, 'text':'Some Site #1'},
        {'lat':37.412061929307924, 'lng':-122.08582878112793, 'text':'Other Site #2'},
        {'lat':37.41301636171327, 'lng':-122.0780611038208, 'text':'Other Site #3'}]

    dajax.add_data(points, 'example_draw_points')
    dajax.assign('#example_log', 'value', "3 Points loaded...")
    return dajax.json()


def move_point(request, lat, lng):
    dajax = Dajax()
    message = "Saved new location at, %s, %s" % (lat, lng)
    dajax.assign('#example_log', 'value', message)
    return dajax.json()


@dajaxice_register
def flickr_save(request, new_title):
    dajax = Dajax()
    dajax.script('cancel_edit();')
    dajax.assign('#title', 'value', new_title)
    dajax.alert('Save complete using "%s"' % new_title)
    return dajax.json()


@dajaxice_register
def pagination(request, p):

    items = get_pagination_page(p)
    render = render_to_string('examples/dajax/pagination_page.html', {'items': items})

    dajax = Dajax()
    dajax.assign('#pagination', 'innerHTML', render)
    return dajax.json()
