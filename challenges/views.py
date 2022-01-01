from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.shortcuts import render
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Eat no meat for the entire month.",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Learn HTML for at least 20 minutes every day!",
    "may": "Learn CSS for at least 20 minutes every day!",
    "june": "Learn Javascript for at least 20 minutes every day!",
    "july": "Learn React for at least 20 minutes every day!",
    "august": "Learn React Native for at least 20 minutes every day!",
    "september": "Learn React JS for at least 20 minutes every day!",
    "october": "Learn Python for at least 20 minutes every day!",
    "november": "Learn PostgreSQL for at least 20 minutes every day!",
    "december": None,
}


def index(request):
    # list_items = ""
    months = list(monthly_challenges.keys())
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)
    context = {
        'months': months,
    }
    return render(request, 'challenges/index.html', context)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid month.</h1>")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        context = {
            'text': challenge_text,
            'month_name': month.capitalize(),
        }
        return render(request, 'challenges/challenge.html', context)
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
        raise Http404()
