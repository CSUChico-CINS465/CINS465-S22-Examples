from django.shortcuts import render
from django.http import HttpResponse

from . import models

# Create your views here.
def index(request, page=0):
    data_list = models.SuggestionModel.objects.all()
    context = {
        "title": "CINS465",
        "paragraph": "hello",
        "data": data_list,
    }
    return render(request, "index.html", context=context)