from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Account, Note
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def vulnerable_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse("Invalid credentials", status=401)
    return render(request, 'notes/login.html')

@login_required
def view_note(request, note_id):
    #account, _ = Account.objects.get_or_create(user=request.user)
    #try:
    #    note = Note.objects.get(id=note_id, account=account)
    #except Note.DoesNotExist:
    #    return HttpResponse("Forbidden", status=403)
    note = Note.objects.get(id=note_id)
    return render(request, 'notes/note_detail.html', {'note': note})

@login_required
def delete_note(request, note_id):
    #account, _ = Account.objects.get_or_create(user=request.user)
    #note = Note.objects.filter(id=note_id, account=account)
    #if note.exists():
    #    note.delete()
    #    return redirect('index')
    #else:
    #    return HttpResponse("Forbidden", status=403)
    Note.objects.filter(id=note_id).delete()
    return redirect('index')

@csrf_exempt
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def index(request):
    # account, _ = Account.objects.get_or_create(user=request.user)
    # notes = Note.objects.filter(account=account)
    username = request.user.username

    notes = Note.objects.raw(
        f"SELECT notes_note.* FROM notes_note "
        f"JOIN notes_account ON notes_note.account_id = notes_account.id "
        f"WHERE notes_account.name = '{username}'"
    )
    
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