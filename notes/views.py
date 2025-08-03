from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView

from .models import Notes


class NotesListView(ListView):
    model = Notes
    context_object_name = "notes" 
    template_name = "notes/notes_list.html"


class PopularNotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    querryset = Notes.objects.filter(likes__gte=1)



def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html',{'notes':all_notes})

class DetailView(DetailView):
    model =  Notes
    context_object_name = "note"


def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note Does Not Exist")
    return render (request, 'notes/notes_detail.html', {'note':note})