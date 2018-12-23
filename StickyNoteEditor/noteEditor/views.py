from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserForm, NoteForm
from .models import StickyNote

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'noteEditor/index.html')
    context = {
        "form": form,
    }
    return render(request, 'noteEditor/register.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'noteEditor/index.html')
            else:
                return render(request, 'noteEditor/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'noteEditor/login.html', {'error_message': 'Invalid login'})
    return render(request, 'noteEditor/login.html')

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'noteEditor/login.html', context)    

def add_note(request):
	if not request.user.is_authenticated:
		return render(request, 'noteEditor/login.html')
	else:
		form = NoteForm(request.POST or None)
		if form.is_valid():
			addNote = form.save(commit=False)
			addNote.user = request.user
			addNote.save()
			form = NoteForm()
			context = {"form":form, 'noteAdded':'Note Successfully Added'}
			return render(request, 'noteEditor/add_note.html', context)
		else:
			context = {"form":form}
			return render(request, 'noteEditor/add_note.html', context)	

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'noteEditor/index.html')
    else:
    	savedNotes = StickyNote.objects.filter(user=request.user)
    	return render(request, 'noteEditor/index.html', {'savedNotes':savedNotes})

