from django.http import HttpResponse
from django.shortcuts import redirect



def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func



def allowed_users(allowed_roles=[]):
    def decorator(viev_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return viev_func(request, *args, **kwargs)
            else:
                return HttpResponse("Sizga bu sahifani ko'rish uchun ruxsat berilmagan")
        return wrapper_func
    return decorator





def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'owner':
            return redirect('user_page', pk=request.user.id)

        elif group == 'admin':
            return view_func(request, *args, **kwargs)

        else:
            return HttpResponse("Sizga bu sahifani ko'rish uchun ruxsat berilmagan")

    return wrapper_func


