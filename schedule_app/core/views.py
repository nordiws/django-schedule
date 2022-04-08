from django.shortcuts import render
from core.models import Event

# Create your views here.
def events_list(request):
    events = Event.objects.all()
    data = {'events': events}
    return render(request, 'schedule.html', data)