from django.urls import path
from . import views

app_name = 'album'

urlpatterns = [
    path('', views.home, name='home'),
    path('add-new-musician/', views.form, name='add_new_musician'),

    path('add-new-album/', views.albumForm, name='add_new_album'),
    path('musician-profile/<int:id>/', views.albumList, name='album_list'),
    path('edit-data/<int:artist_id>/', views.editData, name='edit_data'),
    path('delete-musician-data/<int:artist_id>/',
         views.deleteMusicianData, name='delete_musician_data'),
    path('edit-album-data/<int:artist_id>/<int:album_id>/',
         views.editAlbumList, name='edit_album_data'),
    path('delete-album-data/<int:album_id>/<int:artist_id>/',
         views.deleteAlbumData, name='delete_album_data'),
]
