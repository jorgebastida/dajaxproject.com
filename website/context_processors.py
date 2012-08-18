def js_library(request):
    library = request.GET.get('js', None)
    if library not in ['jquery', 'prototype', 'mootools', 'dojo']:
        library = 'jquery'
    return {'js_library': library}
