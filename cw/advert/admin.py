from django.contrib import admin
from advert.models import Advert

list_display = [
    'id',
    'title',
    'created_at'
]
fields = [
    'title',
    'description',
    'picture',
    'created_at',
    'publicated_at',
    'moderated_at'
]

admin.site.register(Advert)