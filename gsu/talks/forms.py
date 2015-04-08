from django import forms

from talks.models import Talk


class SubmitProposalForm(forms.ModelForm):

    class Meta:
        model = Talk

        fields = (
            'title',
            'speaker',
            'datetime',
        )
