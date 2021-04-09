from django.http import HttpResponse
from django.utils.translation import gettext
from django.utils.translation import ngettext
from django.shortcuts import render

def index(request):
    # Change this number to see how it affects plurals
    objectsCount = 2

    simpleStringTranslated = gettext('Simple string')
    pluralStringTranslated = ngettext(
            'There is %(count)s object',
            'There are %(count)s objects',
            objectsCount,
        ) % {
            'count': objectsCount,
        }

    return render(request, 'django_i18n_example/index.html', {
        'simpleString': simpleStringTranslated,
        'pluralString': pluralStringTranslated,
        'objectsCount': objectsCount,
    })