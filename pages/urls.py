from django.urls import path
from pages.views import *

app_name = "pages"

urlpatterns = [
    path("contact/", contact_page_view, name="contact"),
    path("restaurant/", restaurant_page_view, name="rest"),
    path("activities/", activities_page_view, name="activ"),
    path("about/", about_page_view, name="about"),
    path("booking", home_page_view, name="booking"),
    path("", home_page_view, name="home"),
]