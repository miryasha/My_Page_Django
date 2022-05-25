from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "january Eat no meat for the entire month!",
    "february": " februaryWalk for at least 20 minutes every day!",
    "march": " marchLearn Django for at least 20 minutes every day!",
    "april": " aprilEat no meat for the entire month!",
    "may": " may Walk for at least 20 minutes every day!",
    "june": "Ljune earn Django for at least 20 minutes every day!",
    "july": "july Eat no meat for the entire month!",
    "august": "august Walk for at least 20 minutes every day!",
    "september": "september Learn Django for at least 20 minutes every day!",
    "october": "october Eat no meat for the entire month!",
    "november": "november Walk for at least 20 minutes every day!",
    "december": None,
}

# Create your views here.

def index(request):
    # list_items = ""
    months = list(monthly_challenges.keys())

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # # "<li><a href="...">January</a></li><li><a href="...">February</a></li>..."

    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)
    return render( request, "challenges/index.html", {
        "months": months
    })



def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month.capitalize(),
        })
        # return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")