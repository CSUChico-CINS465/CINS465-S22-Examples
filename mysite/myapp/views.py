from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request, page=0):
    data_list = range(10*page,(page+1)*10,1)
    context = {
        "title": "CINS465",
        "paragraph": "hello",
        "data": data_list,
        "page":page,
        "next": page+1,
        "prev": page-1
    }
    return render(request, "index.html", context=context)