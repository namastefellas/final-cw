from django.shortcuts import render, redirect, get_object_or_404, reverse
from advert.models import Advert
from django.views.generic import ListView

class AdvertModerate(ListView):
    template_name = 'advert/ad_list.html'
    model = Advert
    context_object_name = 'adverts'
    ordering = ('-created_at',)

