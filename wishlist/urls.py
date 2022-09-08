from django.urls import path
# from django.conf.urls import url, include
from wishlist.views import show_wishlist

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
]