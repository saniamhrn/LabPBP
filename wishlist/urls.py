from django.urls import path
# from django.conf.urls import url, include
from wishlist.views import show_wishlist
from wishlist.views import show_xml_wishlist
from wishlist.views import show_json_wishlist
from wishlist.views import show_json_by_id
from wishlist.views import register
from wishlist.views import login_user
from wishlist.views import logout_user

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_xml_wishlist, name='show_xml_wishlist'),
    path('json/', show_json_wishlist, name='show_json_wishlist'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]