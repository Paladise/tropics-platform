from datetime import datetime
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Sand, SandView, SandTeacher
from waters.models import Water

from .forms import TeacherForm


@login_required
def index(request):
    sands = Sand.objects.all()
    return render(request, "sands/index.html", {"sands": sands})


@login_required
def sand(request, id, the_slug):
    sand = Sand.objects.get(id=id)
    if not SandView.objects.filter(sand=sand,session=request.session.session_key):
        view = SandView(sand=sand, session=request.session.session_key)
        view.save()
    num_views = SandView.objects.filter(sand=sand).count()
    waters = Water.objects.filter(sand=sand)
    go_to_water = ""
    teacher_form = TeacherForm()
    if request.method == "POST":
        data = request.POST.dict()
        if "content" in data:
            content = data["content"]
            content = content.replace('"', '\\"')
            content = content.replace("'", "\\'")

            if not Water.objects.filter(content=content, author=request.user, sand=sand).exists():
                water = Water(content=content, author=request.user, sand=sand)
                water.save()
                go_to_water = water.id
                messages.add_message(request, messages.SUCCESS, "Added water")
        elif "remove_mango" in data:
            water = Water.objects.get(id=data["remove_mango"])
            if request.user.gave_mangoes.filter(id=water.id).exists():
                request.user.gave_mangoes.remove(water)
                water.mangoes -= 1
                water.save()
                go_to_water = water.id
                messages.add_message(request, messages.SUCCESS, "Removed mango")
        elif "give_mango" in data:
            water = Water.objects.get(id=data["give_mango"])
            if request.user == water.author:
                messages.add_message(request, messages.ERROR, "Can't give mango to your own water!")
            elif not request.user.gave_mangoes.filter(id=water.id).exists():
                request.user.gave_mangoes.add(water)
                water.mangoes += 1
                water.save()
                go_to_water = water.id
                messages.add_message(request, messages.SUCCESS, "Gave mango")
        elif "delete" in data and Water.objects.filter(id=data["delete"]).exists():
            water = Water.objects.get(id=data["delete"])
            water.delete()
            messages.add_message(request, messages.SUCCESS, "Deleted water")
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
    
    return render(request, 'sands/sand.html', {"sand": sand, "waters": waters, "num_views": num_views, "go_to_water": go_to_water, "teacher_form": teacher_form})