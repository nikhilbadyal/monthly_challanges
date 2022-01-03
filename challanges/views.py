from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

monthly_challanges = {
    'january': 'this is jan',
    'february': 'this is feb',
    'march': 'this is march',
    'april': 'this is april',
    'may': 'this is may',
    'june': 'this is june',
    'july': 'this is july',
}


def monthly_response(request, month):
    try:
        return HttpResponse(monthly_challanges[month])
    except KeyError:
        return HttpResponseNotFound('Some weird month')


def monthly_response_by_number(request, month):
    if month == 1:
        return HttpResponse('This is int jan')
    elif month == 2:
        return HttpResponse('This is int Feb')
    else:
        return HttpResponseNotFound('Month doesn\'t exist on planet Earth')
