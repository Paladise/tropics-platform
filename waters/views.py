from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from datetime import datetime

from .models import Water

from tropics.decorators import not_banned


def user_can_moderate(user, author):
    return author.id == user.id or user.has_management_permission()

@login_required
@not_banned
def go_to_sand(request, id):
    water = Water.objects.get(id=id)
    redirect_url = reverse("sands:sand", args=(water.sand.id,water.sand.slug))
    return redirect(f"{redirect_url}#{id}")


@login_required
@not_banned
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
                water.date_edited = datetime.now()
                water.save()
                messages.add_message(request, messages.SUCCESS, "Edited water")
            redirect_url = reverse("sands:sand", args=(water.sand.id, water.sand.slug))
            return redirect(f"{redirect_url}#{id}")
        else:
            return render(request, 'waters/edit.html', {"water": water})
    else:
        return render(request, 'waters/edit.html', {"water": water})

@login_required
@not_banned
def delete(request, id):
    water = Water.objects.get(id=id)
    if not user_can_moderate(request.user, water.author) or request.method != "POST" or water.deleted:
        return render(request, '404.html')
    
    water.deleted = True
    water.save()
    messages.add_message(request, messages.SUCCESS, "Deleted water")
    redirect_url = reverse("sands:sand", args=(water.sand.id, water.sand.slug))
    return redirect(redirect_url)
    
    
@login_required
@not_banned
def undelete(request, id):
    water = Water.objects.get(id=id)
    if not user_can_moderate(request.user, water.author) or request.method != "POST" or not water.deleted:
        return render(request, '404.html')
    
    water.deleted = False
    water.save()
    messages.add_message(request, messages.SUCCESS, "Undeleted water")
    redirect_url = reverse("sands:sand", args=(water.sand.id, water.sand.slug))
    return redirect(f"{redirect_url}#{id}")
    
    
@login_required
@not_banned
def give_mango(request, id):
    water = Water.objects.get(id=id)
    if request.method != "POST" or request.user.gave_mangoes.filter(id=id).exists():
        return render(request, '404.html')
    if request.user == water.author:
        messages.add_message(request, messages.ERROR, "Can't give mango to your own water!")
    else:
        request.user.gave_mangoes.add(water)
        water.mangoes += 1
        water.save()
        messages.add_message(request, messages.SUCCESS, "Gave mango")
    
    redirect_url = reverse("sands:sand", args=(water.sand.id, water.sand.slug))
    return redirect(f"{redirect_url}#{id}")


@login_required
@not_banned
def take_back_mango(request, id):
    water = Water.objects.get(id=id)
    if request.method != "POST" or not request.user.gave_mangoes.filter(id=id).exists():
        return render(request, '404.html')
    if request.user == water.author:
        messages.add_message(request, messages.ERROR, "Can't take mango from your own water!")
    else:
        request.user.gave_mangoes.remove(water)
        water.mangoes -= 1
        water.save()
        messages.add_message(request, messages.SUCCESS, "Took back mango")
    
    redirect_url = reverse("sands:sand", args=(water.sand.id, water.sand.slug))
    return redirect(f"{redirect_url}#{id}")


