from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from datetime import datetime

from .models import Water


@login_required
def go_to_sand(request, id):
    water = Water.objects.get(id=id)
    redirect_url = reverse("sands:sand", args=(water.sand.id,water.sand.slug))
    return redirect(f"{redirect_url}#{id}")


@login_required
def edit(request, id):
    water = Water.objects.get(id=id)
    if not user_can_moderate(request.user, water.author):
        return render(request, '404.html')

    if request.method == "POST":
        print("Request:", request)
        data = request.POST.dict()
        if "content" in data:
            content = data["content"]
            content = content.replace('"', '\\"')
            content = content.replace("'", "\\'")

            if water.content != content:
                water.content = content
                water.save()
                messages.add_message(request, messages.SUCCESS, "Edited water")
            redirect_url = reverse("sands:sand", args=(water.sand.id, water.sand.slug))
            return redirect(f"{redirect_url}#{id}")
        else:
            return render(request, 'waters/edit.html', {"water": water})
    else:
        return render(request, 'waters/edit.html', {"water": water})


def user_can_moderate(user, author):
    return author.id == user.id or user.has_management_permission()
