from django.shortcuts import render, redirect
from .models import Note, Tag


def index(request):
    if request.method == 'POST':
        note=Note()
        title=request.POST.get('title')
        content=request.POST.get('content')
        tagName = request.POST.get('tag')
        
        note.title=title
        note.content=content

        tag, create = Tag.objects.get_or_create(name=tagName)
        if create:
            tag.save()
        
        note.tag = tag
        note.save()
        return redirect('index')
    else:
        allNotes = Note.objects.all()
        allTags = Tag.objects.all()
        return render(request, 'notes/buttons.html', {'notes': allNotes, 'tags': allTags})


def deleteNote(request, id):
    note=Note.objects.get(id=id)
    note.delete()
    return redirect('index')


def updateNote(request,id):
    tagName = request.POST.get('tag')
    print(tagName)
    tag, create = Tag.objects.get_or_create(name=tagName)
    if create:
        tag.save()
        
    Note.objects.filter(id=id).update(title=request.POST.get('title'), content=request.POST.get('content'), tag=tag)
    return redirect('index')

def tagList(request):
    allTags = Tag.objects.all()
    return render(request, 'tags/tagList.html', {'tags': allTags})

def tagDetails(request,tagId):
    notes = Note.objects.filter(tag=tagId)
    tag=Tag.objects.get(id=tagId)
    return render(request, 'tags/tagDetail.html', {'tag':tag,'notes': notes})