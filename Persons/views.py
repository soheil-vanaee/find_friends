# views.py
from django.shortcuts import render,redirect
from .models import Persons
from .forms import SearchForm, PersonForm
from django.db.models import Q

def index(request):
    persons = Persons.objects.all()
    search_form = SearchForm()
    result = None

    if 'search_query' in request.GET:
        search_query = request.GET['search_query']
        result = persons.filter(
            Q(name__icontains=search_query) |
            Q(family__icontains=search_query) |
            Q(phone__icontains=search_query) |
            Q(email__icontains=search_query)
        )

    return render(request, 'Home/index.html', {'persons': persons, 'search_form': search_form, 'result': result})



from .models import FormEntry
from .forms import FormEntryForm

def form_entry_view(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PersonForm()

    return render(request, 'form_entry.html', {'form': form})

def success_view(request):
    return render(request, 'status/success.html')

def already_filled_view(request):
    return render(request, 'status/already_filled.html')
