from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Family

# Create your views here.
def show_members(request):
    members = Family.objects.all()
    return render(request,'membertemplate.html', {
        "members" : members
    })
