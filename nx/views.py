from django.shortcuts import render_to_response
from django.views.generic import CreateView

from .forms import NotesSearchForm, NotesForm, NeedsForm

from nx.models import Note, Need

def notes(request):
    form = NotesSearchForm(request.GET)
    notes = form.search()
    return render_to_response('notes.html', {'notes': notes})

def search_needs(request):
    form = NotesSearchForm(request.GET)
    notes = form.search()
    return render_to_response('needs.html', {'notes': notes})

class NoteCreate(CreateView):
    """
    Link creation view - assigns the user to the new link, as well
    as setting Mezzanine's ``gen_description`` attribute to ``False``,
    so that we can provide our own descriptions.
    """

    form_class = NotesForm
    model = Note

class NeedCreate(CreateView):
    form_class = NeedsForm
    model = Need
