from django.views.generic import DetailView
from advert.models import Advert

class AdvertDetail(DetailView):
    model = Advert
    template_name = 'advert/ad_view.html'