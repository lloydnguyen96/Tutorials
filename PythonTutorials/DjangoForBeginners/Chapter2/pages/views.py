from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homePageView(request):
    """TODO: Docstring for homePageView.

    :request: TODO
    :returns: TODO

    """
    return HttpResponse('Hello, World!')
