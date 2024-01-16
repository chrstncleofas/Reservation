from app import views
from django.urls import path
from django.conf.urls import url

urlpatterns=[
    url(r'^reservation$',views.reservationApi),
    url(r'^reservation/([0-9]+)$',views.reservationApi),
    # Backend UI
    path('', views.home, name='home'),
    path('list/', views.list, name='list'),
    path('<int:id>', views.list_item, name='list_item'),
    path('edit_list/<int:id>', views.edit_list, name='edit_list'),
    path('delete_list/<int:id>', views.delete_list, name='delete_list'),
]
