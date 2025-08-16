from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('add', views.addPageView, name='add'),
    path('clear', views.erasePageView, name='clear'),
    path('logout', views.logout_view, name='logout')
]