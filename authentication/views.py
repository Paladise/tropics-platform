from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "auth/index.html")

def about(request):
    return render(request, "auth/about.html")

def login_excluded(redirect_to):
    """ This decorator kicks authenticated users out of a view """
    def _method_wrapper(view_method):
        def _arguments_wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_to)
            return view_method(request, *args, **kwargs)
        return _arguments_wrapper
    return _method_wrapper

@login_excluded('authentication:index')
def login(request: HttpRequest) -> HttpResponse:
    return render(request, "auth/login.html")


def error(request: HttpRequest) -> HttpResponse:
    return render(request, "auth/error.html")

