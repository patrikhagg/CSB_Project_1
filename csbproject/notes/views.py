from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Account

@login_required
def index(request):
	items = request.session.get('items', [])

	return render(request, 'notes/index.html', {'items' : items})

@login_required
def addPageView(request):
	items = request.session.get('items', [])

	new_note = request.POST.get('content')
	if new_note:
		items.append(new_note)
		items = items[-10:]
		request.session['items'] = items

	return render(request, 'notes/index.html', {'items' : items})

@login_required
def erasePageView(request):
	request.session['items'] = []

	return render(request, 'notes/index.html', {'items' : []})
