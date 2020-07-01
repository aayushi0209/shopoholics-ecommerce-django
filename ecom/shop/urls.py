# ALL URLS OF SHOP ARE LINKED TO THIS !!!!!

from django.contrib import admin
from django.urls import path
from.import views


urlpatterns = [
    path("", views.index,name="ShopHome"),
    path("about/", views.about,name="About Us"),
    path("contact/", views.contact,name="Contact Us"),
    path("tracker/", views.tracker,name="TrackingStatus"),
    path("search/", views.search,name="Search"),
    path("prodview/<int:myid>", views.prodview ,name="ProductView"),
    path("checkout/", views.checkout,name="Checkout")

]
