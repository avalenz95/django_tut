from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.list import ListView
#Import event class
from myclub_app.models import Event

# Create your views here.


#function based view
def hello_world(request):
    return HttpResponse("<h1>Hello World</h1>")



#class based view
class ClubView(ListView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')

class EventView(View):
    model = Event

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    pass