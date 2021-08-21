from django.urls.base import reverse_lazy
from django.views.generic import DeleteView
from advert.models import Advert
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class AdvertDelete(PermissionRequiredMixin, DeleteView):
    model = Advert
    template_name = 'advert/ad_delete.html'
    context_object_name = 'advert'
    success_url = reverse_lazy('advert:advert_view')
    permission_required = 'advert.delete_advert'