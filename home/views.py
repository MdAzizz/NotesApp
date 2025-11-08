from django.shortcuts import render, redirect
from .models import NotesApp

def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        NotesApp.objects.create(title=title, content=content)
        return redirect('/')  # refresh page after adding note

    notes = NotesApp.objects.all().order_by('-id')
    return render(request, "index.html", {'notes': notes})

def delete_note(request, id):
    note = NotesApp.objects.get(id=id)
    note.delete()
    return redirect('home')