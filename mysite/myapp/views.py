from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from . import models
from . import forms

# Create your views here.
def index(request, page=0):
    if request.method == "POST":
        if request.user.is_authenticated:
            form = forms.SuggestionForm(request.POST)
            if form.is_valid():
                form.save(request)
                form = forms.SuggestionForm()
        else:
            form = forms.SuggestionForm()
    else:
        form = forms.SuggestionForm()
    data_list = []
    suggestion_list = models.SuggestionModel.objects.all()
    for sugg in suggestion_list:
        sugg_instance = {}
        sugg_instance["suggestion"] = sugg.suggestion
        sugg_instance["author"] = sugg.author.username
        comment_list = models.CommentModel.objects.filter(suggestion=sugg)
        sugg_instance["comments"] = []
        sugg_instance["num_comms"] = len(comment_list)
        for comm in comment_list:
            comm_instance = {}
            comm_instance["comment"] = comm.comment
            comm_instance["author"] = comm.author.username
            sugg_instance["comments"] += [comm_instance]
        data_list+=[sugg_instance]



    context = {
        "title": "CINS465",
        "paragraph": "hello",
        "data": data_list,
        "form": form,
    }
    return render(request, "index.html", context=context)

def suggestion_view(request):
    if request.method == "GET":
        data_list = {}
        data_list["suggestions"] = []
        suggestion_list = models.SuggestionModel.objects.all()
        for sugg in suggestion_list:
            sugg_instance = {}
            sugg_instance["suggestion"] = sugg.suggestion
            sugg_instance["author"] = sugg.author.username
            comment_list = models.CommentModel.objects.filter(suggestion=sugg)
            sugg_instance["comments"] = []
            sugg_instance["num_comms"] = len(comment_list)
            for comm in comment_list:
                comm_instance = {}
                comm_instance["comment"] = comm.comment
                comm_instance["author"] = comm.author.username
                sugg_instance["comments"] += [comm_instance]
            data_list["suggestions"].append(sugg_instance)
        return JsonResponse(data_list)
    return HttpResponse("You're doing it wrong")