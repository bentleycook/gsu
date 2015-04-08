
from django.conf.urls import include, url
from django.contrib import admin

from talks.views import SubmitProposalView

urlpatterns = [
    url(r'^submit-proposal/', SubmitProposalView.as_view(), name='submit_proposal'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'talks.views.home', name='home'),
]
