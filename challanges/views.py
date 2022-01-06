from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.
from django.urls import reverse

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
        return HttpResponseNotFound('Month doesn\'t exist on planet Earth YET')


def monthly_response_by_number(request, month):
    months = list(monthly_challanges.keys())
    redirect_month = 'Error'
    try:
        redirect_month = months[month - 1]
        url_base_path = reverse('monthly-challanges', args=[redirect_month])
        return HttpResponseRedirect(url_base_path)

    except IndexError:
        return HttpResponseRedirect('/challanges/' + redirect_month)


