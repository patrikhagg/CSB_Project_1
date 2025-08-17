from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('add', views.addPageView, name='add'),
    path('clear', views.erasePageView, name='clear'),
    path('logout', views.logout_view, name='logout'),
    path('note/<int:note_id>/', views.view_note, name='view_note'),
    path('note/<int:note_id>/delete/', views.delete_note, name='delete_note')
]