from django.views.generic import TemplateView
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render
from .forms import ExampleForm

# Index ################################


class Index(TemplateView):
    template_name = 'website/index.html'


# Dajaxice examples ####################

class DajaxiceExample(TemplateView):
    template_name = 'examples/dajaxice/dajaxice_example.html'


class DajaxiceArgsExample(TemplateView):
    template_name = 'examples/dajaxice/dajaxice_args_example.html'


# Dajax examples #######################

class MultiplyExample(TemplateView):
    template_name = 'examples/dajax/multiply_example.html'


class MapsExample(TemplateView):
    template_name = 'examples/dajax/google_map_example_page.html'


class RandomExample(TemplateView):
    template_name = 'examples/dajax/random_example.html'


class FormExample(TemplateView):
    template_name = 'examples/dajax/form_example.html'


class FlickrExample(TemplateView):
    template_name = 'examples/dajax/flickr_example.html'


def get_pagination_page(page=1):
    items = range(0, 100)
    paginator = Paginator(items, 10)
    try:
        page = int(page)
    except ValueError:
        page = 1

    try:
        items = paginator.page(page)
    except (EmptyPage, InvalidPage):
        items = paginator.page(paginator.num_pages)

    return items


def pagination_example(request):
    items = get_pagination_page(1)
    return render(request, 'examples/dajax/pagination_example.html', {'items': items})


def full_form_example(request):
    example_form = ExampleForm()
    return render(request, 'examples/dajax/full_form_example.html', {'form': example_form})
