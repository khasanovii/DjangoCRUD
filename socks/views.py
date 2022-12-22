from django.shortcuts import render

# relative import of forms
from .models import GeeksModel
from .forms import GeeksForm
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello Geeks")
def create_view(request):
    # dictionary for intial data with
    # field names as keys 
    context = {}

    # add the dictionary during initialization
    form = GeeksForm(request.POST or None)
    if form.is_valid():
       form.save()

    context['form'] = form
    return render(request, "create_view.html", context)   