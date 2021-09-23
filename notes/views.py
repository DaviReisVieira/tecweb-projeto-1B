from django.shortcuts import render, redirect
from .models import Note, Tag


def index(request):
    if request.method == 'POST':
        note=Note()
        title=request.POST.get('title')
        content=request.POST.get('content')
        tagName = request.POST.get('tag')
        
        print(tagName)
        note.title=title
        note.content=content

        print(tagName)
        tag, create = Tag.objects.get_or_create(name=tagName)
        if create:
            tag.save()
        
        note.tag = tag
        note.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/notes.html', {'notes': all_notes})

def updateNoteView(request,id):
    tagName = request.POST.get('tag')
    print(tagName)
    tag, create = Tag.objects.get_or_create(name=tagName)
    if create:
        tag.save()
    Note.objects.filter(id=id).update(title=request.POST.get('title'), content=request.POST.get('content'), tag=tag)
    return redirect('index')


def deleteNoteView(request, id):
    note=Note.objects.get(id=id)
    note.delete()
    return redirect('index')