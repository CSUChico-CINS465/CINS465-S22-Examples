from django.shortcuts import render
from django.http import HttpResponse

from . import models
from . import forms

# Create your views here.
def index(request, page=0):
    if request.method == "POST":
        form = forms.SuggestionForm(request.POST)
        if form.is_valid():
            form.save()
            form = forms.SuggestionForm()
    else:
        form = forms.SuggestionForm()
    data_list = models.SuggestionModel.objects.all()

    context = {
        "title": "CINS465",
        "paragraph": "hello",
        "data": data_list,
        "form": form,
    }
    return render(request, "index.html", context=context)