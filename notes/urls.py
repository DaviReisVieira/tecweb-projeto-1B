from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:id>', views.deleteNoteView, name='delete'),
    path('update/<int:id>', views.updateNoteView, name='update'),
]