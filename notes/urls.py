from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:id>', views.updateNote, name='update'),
    path('delete/<int:id>', views.deleteNote, name='delete'),
    path('tags', views.tagList, name='tags'),
    path('tags/<int:tagId>', views.tagDetails, name='tag_details')
]