
# Create your views here.
from django.shortcuts import render, redirect
from .forms import EventForm

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EventForm()
    return render(request, 'event_create.html', {'form': form})
