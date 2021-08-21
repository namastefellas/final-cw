from advert.models import Advert
from django.views.generic import UpdateView
from django.shortcuts import reverse
from advert.forms import AdvertForm

class AdvertUpdate(UpdateView):
    form_class = AdvertForm
    model = Advert
    template_name = 'advert/ad_edit.html'
    context_object_name = 'advert'

    def form_valid(self, form):
        advert = form.save(commit=False)