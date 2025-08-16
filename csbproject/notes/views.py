from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Account, Note
from django.contrib.auth import logout

@login_required
def index(request):
    account, _ = Account.objects.get_or_create(user=request.user)
    notes = Note.objects.filter(account=account)
    return render(request, 'notes/index.html', {'items': notes})

@login_required
def addPageView(request):
    account, _ = Account.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        new_note = request.POST.get('content')
        if new_note:
            Note.objects.create(account=account, content=new_note)
    notes = Note.objects.filter(account=account)
    return render(request, 'notes/index.html', {'items': notes})

@login_required
def erasePageView(request):
    account, _ = Account.objects.get_or_create(user=request.user)
    Note.objects.filter(account=account).delete()
    return render(request, 'notes/index.html', {'items': []})

def logout_view(request):
    logout(request)
    return redirect('login')