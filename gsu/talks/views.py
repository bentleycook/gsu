
from django.shortcuts import render

from talks.models import Talk


def home(request):

    talks = Talk.objects.all()

    return render(
        request,
        'talks/index.html',
        {'talks': talks}
    )
