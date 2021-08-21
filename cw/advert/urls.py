from django.urls import path
from advert.views.adverts.advertlist import AdvertList
from advert.views.adverts.advertdetail import AdvertDetail
from advert.views.adverts.advertupdate import AdvertUpdate
from advert.views.adverts.advertdelete import AdvertDelete
from advert.views.adverts.advertcreate import AdvertCreate
from advert.views.adverts.advertmoderate import AdvertModerate

app_name = 'advert'

urlpatterns = [
    path('', AdvertList.as_view(), name='advert_list'),
    path('<int:pk>/view/', AdvertDetail.as_view(), name='advert_view'),
    path('<int:pk>/edit/', AdvertUpdate.as_view(), name='advert_edit'),
    path('<int:pk>/delete/', AdvertDelete.as_view(), name='advert_delete'),
    path('create/', AdvertCreate.as_view(), name='advert_create'),
    path('moderate/', AdvertModerate.as_view(), name='advert_moderate')
]