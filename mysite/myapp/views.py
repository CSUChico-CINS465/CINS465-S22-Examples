import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required

from . import models
from . import forms

def logout_view(request):
    logout(request)
    return redirect("/login/")

@login_required
def add_comment_view(request, sugg_id):
    if request.method == "POST":
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            form.save(request, sugg_id)
            return redirect("/")
    else:
        form = forms.CommentForm()
    context = {
        "form": form,
        "sugg_id":sugg_id,
    }
    return render(request, "comment.html", context=context)

@login_required
def add_suggestion_view(request):
    if request.method == "POST":
        form = forms.SuggestionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(request)
            return redirect("/")
    else:
        form = forms.SuggestionForm()
    context = {
        "form": form,
    }
    return render(request, "suggestion.html", context=context)

# Create your views here.
@login_required
def index(request):
    data_list = {}
    data_list["suggestions"] = []
    suggestion_list = models.SuggestionModel.objects.all().order_by("-created_on")
    for sugg in suggestion_list:
        sugg_instance = {}
        sugg_instance["suggestion"] = sugg.suggestion
        sugg_instance["id"] = sugg.id
        sugg_instance["author"] = sugg.author.username
        comment_list = models.CommentModel.objects.filter(suggestion=sugg)
        sugg_instance["comments"] = []
        sugg_instance["num_comms"] = len(comment_list)
        if sugg.image:
            sugg_instance["image"] = sugg.image.url
            sugg_instance["image_desc"] = sugg.image_description
        else:
            sugg_instance["image"] = ""
            sugg_instance["image_desc"] = ""
        sugg_instance["date"] = sugg.created_on.strftime("%m/%d/%Y, %I:%M:%S %p")
        for comm in comment_list:
            comm_instance = {}
            comm_instance["comment"] = comm.comment
            comm_instance["author"] = comm.author.username
            sugg_instance["comments"] += [comm_instance]
            time_diff = datetime.datetime.now(datetime.timezone.utc) - comm.created_on
            time_diff_s = time_diff.total_seconds()
            time_format(time_diff_s, comm_instance, comm)
        data_list["suggestions"].append(sugg_instance)
    context = {
        "title": "CINS465",
        "suggestions":data_list["suggestions"]
    }
    return render(request, "index.html", context=context)

def registration_view(request):
    if request.method == "POST":
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login/")
    else:
        form = forms.RegistrationForm()
    context = {
        "title": "Register",
        "form": form,
    }
    return render(request, "registration/registration.html", context=context)

def time_format(time_diff_s, comm_instance, comm):
    if time_diff_s < 60:
        comm_instance["date"] = "published " + str(int(time_diff_s)) + " seconds ago"
    else:
        time_diff_m = divmod(time_diff_s,60)[0]
        if time_diff_m < 60:
            comm_instance["date"] = "published " + str(int(time_diff_m)) + " minutes ago"
        else:
            time_diff_h = divmod(time_diff_m,60)[0]
            if time_diff_h < 24:
                comm_instance["date"] = "published " + str(int(time_diff_h)) + " hours ago"
            else:
                comm_instance["date"] = comm.published_on.strftime("%Y-%m-%d")

def suggestion_view(request):
    if request.method == "GET":
        data_list = {}
        data_list["suggestions"] = []
        suggestion_list = models.SuggestionModel.objects.all().order_by("-created_on")
        for sugg in suggestion_list:
            sugg_instance = {}
            sugg_instance["suggestion"] = sugg.suggestion
            sugg_instance["id"] = sugg.id
            sugg_instance["author"] = sugg.author.username
            comment_list = models.CommentModel.objects.filter(suggestion=sugg)
            sugg_instance["comments"] = []
            sugg_instance["num_comms"] = len(comment_list)
            if sugg.image:
                sugg_instance["image"] = sugg.image.url
                sugg_instance["image_desc"] = sugg.image_description
            else:
                sugg_instance["image"] = ""
                sugg_instance["image_desc"] = ""
            sugg_instance["date"] = sugg.created_on.strftime("%m/%d/%Y, %I:%M:%S %p")
            for comm in comment_list:
                comm_instance = {}
                comm_instance["comment"] = comm.comment
                comm_instance["author"] = comm.author.username
                sugg_instance["comments"] += [comm_instance]
                time_diff = datetime.datetime.now(datetime.timezone.utc) - comm.created_on
                time_diff_s = time_diff.total_seconds()
                time_format(time_diff_s, comm_instance, comm)
            data_list["suggestions"].append(sugg_instance)
        return JsonResponse(data_list)
    return HttpResponse("You're doing it wrong")
