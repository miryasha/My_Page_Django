
from django.urls import path
from . import views


urlpatterns = [
    #here we are definign what endpoit should run our code
    #/challanges/january 
    #path("january", views.january),
    # path("february", views.february)
    path("<month>", views.monthly_challenge)
]