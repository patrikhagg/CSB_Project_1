from django.contrib import admin
from django.urls import include, path
# from django.contrib.auth.views import LoginView, LogoutView
from notes.views import vulnerable_login, logout_view

urlpatterns = [
    path("", include("notes.urls")),
	# path('login/', LoginView.as_view(template_name='notes/login.html')),
	# path('logout/', LogoutView.as_view(), name='logout'),
    path("login/", vulnerable_login, name="login"),
    path("logout/", logout_view, name="logout"),
    path("admin/", admin.site.urls),
]