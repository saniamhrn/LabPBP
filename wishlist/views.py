from django.shortcuts import render
from wishlist.models import BarangWishlist
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_wishlist(request):
        data_barang_wishlist = BarangWishlist.objects.all()
        context = {
                'list_barang': data_barang_wishlist,
                'nama': 'Sania Rizqi Maharani'
        }
        return render(request, "wishlist.html", context)

def show_xml_wishlist(request):
        data_xml = BarangWishlist.objects.all()
        return HttpResponse(serializers.serialize("xml", data_xml), content_type="application/xml")

def show_json_wishlist(request):
        data_json = BarangWishlist.objects.all()
        return HttpResponse(serializers.serialize("json", data_json), content_type="application/json")

def show_json_by_id(request):
        data_json_by_id = BarangWishlist.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json_by_id", data_json_by_id), content_type="application/json_by_id")