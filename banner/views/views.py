from banner.models import Order, Place, Place_owner, Tadbirkor
from django.shortcuts import render, redirect, get_object_or_404

from banner.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from banner.decorators import unauthenticated_user, allowed_users, admin_only
from datetime import date


def change_posts_status():
    Place.objects.filter(
        busy='Band', end_date__lt=date.today()).update(busy="Bo'sh")


def change_order_status():
    Order.objects.filter(status='Active', end_date__lt=date.today()).update(
        status='NotActive')


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():

            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='owner')
            user.groups.add(group)

            messages.success(
                request, f'Yangi hisob {username} uchun yaratildi')

            return redirect('login')

    context = {'form': form}
    return render(request, 'register/register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group == 'owner':
                return redirect('user_page')

            elif group == 'admin':
                return redirect('home')

        else:
            messages.info(request, 'Parol yoki foydalanuvchi nomi hato!')

    context = {}
    return render(request, 'register/login.html', context)


def logOutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@admin_only
def home(request):
    change_posts_status()
    change_order_status()
    orders = Order.objects.all()
    active = orders.filter(status='Active')
    egasi = Place_owner.objects.filter(is_staff=False)


    egalari = []
    for eg in egasi:
        places_count = eg.place_set.all().count()
        dt = {"id": eg.id,
              "username": eg.username,
              "phone": eg.phone,
              "places_count": places_count}
        egalari.append(dt)

    places = Place.objects.all()
    free_places = places.filter(busy="Bo'sh").count()
    busy_places = places.filter(busy="Band").count()

    total_places = places.count()
    total_orders = orders.count()
    total_owners = egasi.count()
    total_tadbirkor = Tadbirkor.objects.all().count()

    context = {
        'active': active,
        'places': places,
        'egalari': egalari,
        'free_places': free_places,
        'busy_places': busy_places,
        'total_places': total_places,
        'total_orders': total_orders,
        'total_owners': total_owners,
        'total_tadbirkor': total_tadbirkor,

    }

    return render(request, 'dashboard.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def order(request):
    change_order_status()
    orders = Order.objects.all()

    history = orders.filter(status='NotActive')
    current_orders = orders.filter(status='Active')

    now_count = current_orders.count()
    history_count = history.count()

    context = {'orders': orders,
               'now_count': now_count,
               'history_count': history_count,
               'history': history,
               'current_orders': current_orders,
               }
    return render(request, 'orders.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def tadbirkor(request):
    tadbirkorlar = Tadbirkor.objects.all()
    tadbirkorlar_soni = Tadbirkor.objects.all().count()
    return render(request, 'tadbirkor.html', {'tadbirkorlar': tadbirkorlar, 'tadbirkorlar_soni': tadbirkorlar_soni})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def tadbirkor_detail(request, pk):
    tadbirkor = get_object_or_404(Tadbirkor, id=pk)
    orders = tadbirkor.order_set.all()
    orders_count = tadbirkor.order_set.all().count()

    context = {
        'tadbirkor': tadbirkor,
        'orders': orders,
        'orders_count': orders_count}
    return render(request, 'tad_detail.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def owners(request):
    change_posts_status()
    places = Place.objects.all()
    free_places = places.filter(busy="Bo'sh").count()
    busy_places = places.filter(busy="Band").count()
    total_places = places.count()

    egalari = Place_owner.objects.filter(is_staff=False)
    total_owners = egalari.count()

    egasi = []
    for ega in egalari:
        places_count = ega.place_set.all().count()
        dt = {
            "id": ega.id,
            "username": ega.username,
            "phone": ega.phone,
            "places_count": places_count
        }
        egasi.append(dt)

    context = {
        'places': places,
        'egasi': egasi,
        'free_places': free_places,
        'busy_places': busy_places,
        'total_places': total_places,
        'total_owners': total_owners,
    }
    return render(request, 'owners.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def owner_detail(request, pk):
    egasi = get_object_or_404(Place_owner, id=pk, is_staff=False)
    places = egasi.place_set.all()
    places_count = egasi.place_set.all().count()
    orders = places.count()

    context = {
        'egasi': egasi,
        'orders': orders,
        'places': places,
        'places_count': places_count,
    }
    return render(request, 'owner_detail.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def joylar(request):
    change_posts_status()
    places = Place.objects.all()

    free_places = places.filter(busy="Bo'sh")
    busy_places = places.filter(busy="Band")

    free_places_count = places.filter(busy="Bo'sh").count()
    busy_places_count = places.filter(busy="Band").count()
    total_places_count = places.count()

    context = {
        'places': places,
        'free_places': free_places,
        'busy_places': busy_places,

        'free_places_count': free_places_count,
        'busy_places_count': busy_places_count,
        'total_places_count': total_places_count,
    }
    return render(request, 'joylar.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def joy_detail(request, pk):

    change_posts_status()
    change_order_status()

    place = get_object_or_404(Place, id=pk)
    orders = place.order_set.all()

    active = orders.filter(status='Active')
    not_active = orders.filter(status='NotActive')

    context = {
        'place': place,
        'orders': orders,
        'active': active,
        'not_active': not_active,
    }
    return render(request, 'joy_detail.html', context)


# User
@login_required(login_url='login')
@allowed_users(allowed_roles=['owner', 'admin'])
def userPage(request):

    change_posts_status()
    change_order_status()

    places = request.user.place_set.all()
    places_count = places.count()

    free_places = places.filter(busy="Bo'sh")
    busy_places = places.filter(busy="Band")

    free_places_count = free_places.count()
    busy_places_count = busy_places.count()

    # active = orders.filter(status='Active')
    # not_active = orders.filter(status='NotActive')

    context = {
        # 'place_owner': place_owner,
        'places': places,
        'free_places': free_places,
        'busy_places': busy_places,
        'places_count': places_count,
        'free_places_count': free_places_count,
        'busy_places_count': busy_places_count,
        # 'orders_count': orders_count,
        # 'active': active,
        # 'not_active': not_active
    }
    return render(request, 'user-place.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def joy_detail(request, pk):

    change_posts_status()
    change_order_status()

    place = get_object_or_404(Place, id=pk)
    orders = place.order_set.all()

    active = orders.filter(status='Active')
    not_active = orders.filter(status='NotActive')

    context = {
        'place': place,
        'orders': orders,
        'active': active,
        'not_active': not_active,
    }
    return render(request, 'joy_detail.html', context)