from django.urls.base import reverse_lazy
from django.views.generic import DeleteView
from advert.models import Advert

class AdvertDelete(DeleteView):
    model = Advert
    template_name = 'advert/ad_delete.html'
    context_object_name = 'advert'
    success_url = reverse_lazy('advert:advert_view')