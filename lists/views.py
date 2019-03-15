from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    page = "<html><title>To-Do lists</title></html>"
    return HttpResponse(page)
