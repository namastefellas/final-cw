from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import CreateView
from advert.models import Advert
from advert.forms import AdvertForm

class AdvertCreate(CreateView):
    template_name = 'advert/ad_create.html' 
    model = Advert
    form_class = AdvertForm

    def form_valid(self, form):
        user = self.request.user
        advert = form.save(commit=False)
        advert.user = user
        advert.save()
        return redirect('advert:advert_list')