from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


#we are passing parameter here which automatically executes
#this is called by Django for incoming request
# def january(request):
#     #this would be response we are sending bach to client

#     return HttpResponse("Hello january")

# def february(request):
#     #this would be response we are sending bach to client

#     return HttpResponse("Hello February")    

def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Hello january"
    elif month == "february": 
        challenge_text = "Hello february"
    else:
         return HttpResponseNotFound("this month is not suportet")    
    return HttpResponse(challenge_text)