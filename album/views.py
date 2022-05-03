from django.shortcuts import render, redirect, HttpResponseRedirect
# from django.http import redirect
from album.models import Musician, Album
from .forms import MusicianForm, AlbumForm
# Create your views here.
from django.db.models import Avg


def home(request):
    musician_list = Musician.objects.order_by('first_name')
    return render(request, 'album/album.html', {'album': musician_list})


def form(request):
    new_form = MusicianForm()
    if(request.method == 'POST'):
        new_form = MusicianForm(request.POST)
        if new_form.is_valid():
            new_form.save(commit=True)
            return home(request)
    return render(request, 'album/form.html', {'form': new_form})


def albumForm(request):
    form = AlbumForm()
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return home(request)
    return render(request, 'album/album_form.html', {'form': form})


def albumList(request, id):
    info = Musician.objects.get(pk=id)
    album = Album.objects.filter(artist=id)
    avg_rating = Album.objects.filter(artist=id).aggregate(Avg('num_stars'))
    return render(request, 'album/album_list.html', {'album_list': album, 'info': info, 'avg_rating': avg_rating})


def editData(request, artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    form = MusicianForm(instance=artist_info)
    if request.method == 'POST':
        form = MusicianForm(request.POST, instance=artist_info)
        if form.is_valid():
            form.save(commit=True)
            return albumList(request, artist_id)
    return render(request, 'album/form.html', {'form': form, 'edit': True})


def editAlbumList(request, artist_id, album_id):
    album_list = Album.objects.get(pk=album_id)
    form = AlbumForm(instance=album_list)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album_list)
        if form.is_valid():
            form.save()
            return albumList(request, artist_id)
    return render(request, 'album/album_form.html', {'form': form, 'edit': True})


def deleteMusicianData(request, artist_id):
    data = Musician.objects.get(pk=artist_id).delete()
    return redirect('/')


def deleteAlbumData(request, album_id, artist_id):
    data = Album.objects.get(pk=album_id).delete()
    return redirect(f"/musician-profile/{artist_id}/")
