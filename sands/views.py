from datetime import datetime
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Sand, SandView, SandTeacher
from waters.models import Water

from .forms import TeacherForm

from tropics.decorators import not_banned


@login_required
@not_banned
def index(request):
    sands = Sand.objects.all()
    return render(request, "sands/index.html", {"sands": sands})


@login_required
@not_banned
def sand(request, id, the_slug):
    sand = Sand.objects.get(id=id)
    if sand.slug != the_slug:
        redirect_url = reverse("sands:sand", args=(id, sand.slug))
        return redirect(redirect_url)
    
    if not SandView.objects.filter(sand=sand,session=request.session.session_key):
        view = SandView(sand=sand, session=request.session.session_key)
        view.save()
    num_views = SandView.objects.filter(sand=sand).count()
    waters = Water.objects.filter(sand=sand)
    go_to_water = ""
    teacher_form = TeacherForm()
    hot_sands = {water.sand for water in Water.objects.filter(deleted = False, author__is_banned = False).order_by('-date_edited')[:3]}
    if request.method == "POST":
        data = request.POST.dict()
        if "content" in data:
            content = data["content"]
            content = content.replace('"', '\\"')
            content = content.replace("'", "\\'")

            if not Water.objects.filter(content=content, sand=sand).exists():
                water = Water(content=content, author=request.user, sand=sand)
                water.save()
                go_to_water = water.id
                messages.add_message(request, messages.SUCCESS, "Added water")
            else:
                messages.add_message(request, messages.ERROR, "Duplicates not allowed!")
        elif "add_teacher" in data:
            form = TeacherForm(request.POST)
            if form.is_valid():
                teacher = form.save(commit=False)
                teacher.sand = sand
                teacher.added_by = request.user
                teacher.save()
                messages.add_message(request, messages.SUCCESS, "Added Teacher")
            else:
                teacher_form = form
    
    return render(request, 'sands/sand.html', {"sand": sand, "waters": waters, "num_views": num_views, "go_to_water": go_to_water, "teacher_form": teacher_form, "hot_sands": hot_sands})