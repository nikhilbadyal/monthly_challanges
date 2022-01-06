"""
Views
"""
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

monthly_challanges = {
    'january': 'this is jan',
    'february': 'this is feb',
    'march': 'this is march',
    'april': 'this is april',
    'may': 'this is may',
    'june': 'this is june',
    'july': 'this is july',
    'august': 'this is august',
    'september': 'this is september',
    'october': 'this is october',
    'november': 'this is november',
    'december': None,
}


def list_of_months(request):
    """
    :param request:
    :return:
    """
    months = monthly_challanges.keys()

    return render(request, "challenges/list_of_months.html", {
        "months": months
    })


def monthly_response_by_number(request, month):
    """

    :param request:
    :param month:
    :return:
    """
    months = list(monthly_challanges.keys())
    redirect_month = 'Error'
    try:
        redirect_month = months[month - 1]
        url_base_path = reverse('monthly-challenges', args=[redirect_month])
        return HttpResponseRedirect(url_base_path)

    except IndexError:
        return HttpResponseRedirect('/challenges/' + redirect_month)


# noinspection PyBroadException
def monthly_response(request, month):
    try:
        challenge = monthly_challanges[month]
        return render(request, "challenges/challenge.html", {
            'month_name': month,
            'challenge_text': challenge,
        })
    except:
        raise Http404()
