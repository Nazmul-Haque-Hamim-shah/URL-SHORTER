from django.urls import path
from . import views
urlpatterns = [
   path("home/",views.Home.as_view()),
   path("shorten/",views.Shorten.as_view()),
   path("s/<str:short_code>/",views.URL_Redirect.as_view()),
   path("custom/",views.Custoom.as_view()),
   path("display/urls/",views.URL_Display.as_view())
]