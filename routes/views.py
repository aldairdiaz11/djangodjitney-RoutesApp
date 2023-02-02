from django.shortcuts import render
from .models import Line, Station, Stop
from .forms import StopForm, LineForm, StationForm
# Add your imports below:
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "routes/home.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["lines"] = Line.objects.all()
        context["stations"] = Station.objects.all()
        context["stops"] = Stop.objects.all()
        return context

# Create your views here.
