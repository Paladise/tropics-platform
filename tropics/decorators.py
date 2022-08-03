from functools import wraps
from django.shortcuts import render

def not_banned(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):
        if not request.user.is_banned:
            return function(request, *args, **kwargs)
        else:
            return render(request, "banned.html")
        
  return wrap