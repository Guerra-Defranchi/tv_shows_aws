from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages

def shows(request):
    shows = Show.objects.all()
    context = {
            'shows': shows,
            }
    return render(request, 'index.html', context)

def add_shows(request):
    return render(request, 'add_shows.html')

def create(request):
    tit = request.POST['title']
    net = request.POST['network']
    date = request.POST['release_date']
    descr = request.POST['description']
    Show.objects.create(
            title = tit,
            network = net,
            description = descr,
            release_date = date
            )
    return redirect('/')

def edit_shows(request, ids):
    selected_show = Show.objects.get(id=ids)
    context = {
            'show': selected_show,
            }
    return render(request, 'edit-shows.html', context)

def update(request, ids):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for value in errors.values():
            messages.error(request, value)
        return redirect('/edit/'+ str(ids))
    else:
        edit = Show.objects.get(id=ids)
        edit.title = request.POST['title']
        edit.network = request.POST['network']
        edit.release_date = request.POST['release_date']
        edit.description = request.POST['description']
        edit.save()
        messages.success(request, 'Show updated successfully')
        return redirect('/edit/' + str(ids))

def pointed_show(request, ids):
    show = Show.objects.get(id=ids)
    context = {
            'show': show
            }
    return render(request, 'display-shows.html', context)

def destroy(request, ids):
    Show.objects.get(id=ids).delete()
    return redirect('/')


# Create your views here.
