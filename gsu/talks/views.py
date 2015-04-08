
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render

from talks.models import Talk
from talks.forms import SubmitProposalForm


def home(request):

    talks = Talk.objects.all()

    return render(
        request,
        'talks/index.html',
        {'talks': talks}
    )


class SubmitProposalView(View):

    def get(self, request):
        return render(
            request,
            'talks/submit.html',
            {'form': SubmitProposalForm()}
        )

    def post(self, request):
        form = SubmitProposalForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(
                request,
                'talks/submit.html',
                {'form': form}
            )
