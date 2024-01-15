from app import views
from django.conf.urls import url

urlpatterns=[
    url(r'^reservation$',views.reservationApi),
    url(r'^reservation/([0-9]+)$',views.reservationApi),
]
