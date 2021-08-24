from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path("",views.index,name="shopHome"),
    path("about/",views.about,name="AboutUs"),
    path("contact/",views.contact,name="contactUs"),
    path("tracker/",views.tracker,name="TrackingStatus"),
    path("search/",views.search,name="Search"),
    path("productView/",views.productView,name="product"),
    path("checkout/",views.checkOut,name="Checkout"),

    

    ]