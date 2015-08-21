from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.views.generic import CreateView
from django.template import RequestContext,loader
from django.http import HttpResponse

from .forms import NotesSearchForm, NeedsSearchForm, NotesForm, NeedsForm

from nx.models import Donate, Need

def notes(request):
    form = NotesSearchForm(request.GET)
    notes = form.search()
    return render_to_response('donates.html', {'donates': notes})

def note(request, note_id=None):
    result = Donate.objects.get(id=note_id)
    return render_to_response('donate_detail.html', {'donate': result})

def need(request, need_id=None):
    result = Need.objects.get(id=need_id)
    return render_to_response('need_detail.html', {'need': result})

def search_needs(request):
    if(request.method == 'POST'):
        kwargs = { request.POST['search_name'] : request.POST['search_value']}
        needs = Need.objects.filter(**kwargs)
    else:
        form = NeedsSearchForm(request.GET)
        needs = form.search()

    t = loader.get_template('needs.html')
    c = RequestContext(request,{'needs': needs})
    return HttpResponse(t.render(c))

class NoteCreate(CreateView):
    """
    Link creation view - assigns the user to the new link, as well
    as setting Mezzanine's ``gen_description`` attribute to ``False``,
    so that we can provide our own descriptions.
    """

    form_class = NotesForm
    model = Donate

    def get_success_url(self):
        return "/note/" + str(self.object.id)

class NeedCreate(CreateView):
    form_class = NeedsForm
    model = Need

    def get_success_url(self):
        return "/need/" + str(self.object.id)
