
from django.urls import path
from . import views


urlpatterns = [
    #here we are definign what endpoit should run our code
    #/challanges/january 
    #path("january", views.january),
    # path("february", views.february)
     path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge)
   
]