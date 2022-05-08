from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.


#we are passing parameter here which automatically executes
#this is called by Django for incoming request
# def january(request):
#     #this would be response we are sending bach to client

#     return HttpResponse("Hello january")

# def february(request):
#     #this would be response we are sending bach to client

#     return HttpResponse("Hello February")    
monthly_challenges = {
    "january":"Hello january",
    "february":"Hello february",
    "march":"Hello march",
    "april":"Hello april"
   
}

def monthly_challenge_by_number(request, month):
    # print(monthly_challenges.keys())
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("invalid month")
    redirect_month = months[month - 1]
    # print(redirect_month)
    return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenge(request, month):
    # challenge_text = None
    # if month == "january":
    #     challenge_text = "Hello january"
    # elif month == "february": 
    #     challenge_text = "Hello february"
    # else:
        #  return HttpResponseNotFound("this month is not suportet")  
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("this month is not suportet") 

      
