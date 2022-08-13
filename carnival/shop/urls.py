from . import views
from django.urls import path

urlpatterns = [
    path("home/",views.index,name="ShopHome"),
    path("about/",views.about,name="AboutUs"),
    path("contact/",views.contact,name="ContactUs"),
    path("tracker/",views.tracker,name="TrackingStatus"),
    path("search/",views.search,name="Search"),
    path("products/<int:myid>",views.productview,name="ProductView"),
    path("chekout/",views.chekout,name="Checkout"),

]
