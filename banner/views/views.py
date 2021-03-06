from django.core import paginator
from banner.models import Order, Place, Place_owner, Tadbirkor
from django.shortcuts import render, redirect, get_object_or_404

from banner.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from banner.decorators import unauthenticated_user, allowed_users, admin_only
from datetime import date
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def change_posts_status():
    Place.objects.filter(busy='Band', end_date__lt=date.today()).update(busy="Bo'sh")


def change_order_status():
    Order.objects.filter(status='Active', end_date__lt=date.today()).update(status='NotActive')

def change_history():
    orders = Order.objects.filter(status='NotActive')
    for ord in orders:
        pl = ord.place
        pl.busy = "Bo'sh"
        pl.save()


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
    ##paginator 
    p = Paginator(egasi, 1)
    page = request.GET.get('page')
    egalari_P = p.get_page(page)
    num_of_egalari = 'a' * egalari_P.paginator.num_pages


    pag = Paginator(active, 2)
    page2 = request.GET.get('page2')
    amalda = pag.get_page(page2)
    num_of_active = 'a' * amalda.paginator.num_pages
    ##endpaginator
    
    places = Place.objects.all()
    free_places = places.filter(busy="Bo'sh").count()
    busy_places = places.filter(busy="Band").count()

    total_places = places.count()
    total_orders = orders.count()
    total_owners = egasi.count()

    context = {
        'active': active,
        'places': places,
        'egalari': egalari,
        'free_places': free_places,
        'busy_places': busy_places,
        'total_places': total_places,
        'total_orders': total_orders,
        'total_owners': total_owners,
        'egalari_P':egalari_P,
        'num_of_egalari':num_of_egalari,
        'amalda': amalda,
        'num_of_active':num_of_active

    }
    return render(request, 'dashboard.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def order(request):
    change_posts_status()
    change_order_status()
    orders = Order.objects.all()

    history = orders.filter(status='NotActive')
    current_orders = orders.filter(status='Active')

    now_count = current_orders.count()
    history_count = history.count()

    #PAGINATOR

    p = Paginator(current_orders, 1)
    page = request.GET.get('page')
    co_P = p.get_page(page)
    num_of_co = 'a' * co_P.paginator.num_pages

    p2 = Paginator(history, 1)
    page2 = request.GET.get('page2')
    history_P = p2.get_page(page2)
    num_of_history = 'a' * history_P.paginator.num_pages

    ##ENDPAGINATOR

    context = {'orders': orders,
               'now_count': now_count,
               'history_count': history_count,
               'history': history,
               'current_orders': current_orders,
               'co_P':co_P,
               'num_of_co':num_of_co,
               'history_P':history_P,
               'num_of_history':num_of_history
               }
    return render(request, 'orders.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def tadbirkor(request):
    tadbirkorlar = Tadbirkor.objects.all()
    tadbirkorlar_soni = tadbirkorlar.count()

    #PAGINATOR
    p = Paginator(tadbirkorlar, 1)
    page = request.GET.get('page')
    tadbirlorlar_P = p.get_page(page)
    num_of_egalari = 'a' * tadbirlorlar_P.paginator.num_pages
    #END PAGINATOR

    context = {
          'tadbirkorlar_soni': tadbirkorlar_soni,
          'num_of_egalari':num_of_egalari,
          'tadbirlorlar_P':tadbirlorlar_P,

      }

    return render(request, 'tadbirkor.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def tadbirkor_detail(request, pk):
    tadbirkor = get_object_or_404(Tadbirkor, id=pk)
    orders = tadbirkor.order_set.all()
    orders_count = tadbirkor.order_set.all().count()
    
    #PAGINATOR
    p = Paginator(orders, 1)
    page = request.GET.get('page')
    order_P = p.get_page(page)
    num_of_order = 'a' * order_P.paginator.num_pages
    #END PAGINATOR
    context = {
        'tadbirkor': tadbirkor,
        'orders_count': orders_count,
        'order_P':order_P,
        'num_of_order':num_of_order
        }
    return render(request, 'tad_detail.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def owners(request):
    change_posts_status()
    change_order_status()
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
    #paginator
    p = Paginator(egasi, 1)
    page = request.GET.get('page')
    egalari_P = p.get_page(page)
    num_of_egalari = 'a' * egalari_P.paginator.num_pages
    # endpaginator
    context = {
        'places': places,
        'egasi': egasi,
        'free_places': free_places,
        'busy_places': busy_places,
        'total_places': total_places,
        'total_owners': total_owners,
        'egalari_P':egalari_P,
        'num_of_egalari':num_of_egalari,
        
    }
    return render(request, 'owners.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def owner_detail(request, pk):
    change_posts_status()
    change_order_status()
    egasi = get_object_or_404(Place_owner, id=pk, is_staff=False)
    places = egasi.place_set.all()
    places_count = places.count()
    context = {
        'egasi': egasi,
        'places': places,
        'places_count': places_count,
    }
    return render(request, 'owner_detail.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def joylar(request):
    change_posts_status()
    change_order_status()
    change_history()
    places = Place.objects.all()
    free_places = places.filter(busy="Bo'sh")
    busy_places = places.filter(busy="Band")
    free_places_count = free_places.count()
    busy_places_count = busy_places.count()
    total_places_count = places.count()
    
    #paginator
    p = Paginator(free_places, 1)
    page = request.GET.get('page')
    free_P = p.get_page(page)
    num_of_free = 'a' * free_P.paginator.num_pages

    p2 = Paginator(busy_places, 1)
    page2 = request.GET.get('page2')
    busy_P = p.get_page(page2)
    num_of_busy = 'a' * busy_P.paginator.num_pages
    # endpaginator

    context = {
        'places': places,
        'free_places_count': free_places_count,
        'busy_places_count': busy_places_count,
        'total_places_count': total_places_count,
        'free_P':free_P,
        'num_of_free':num_of_free,
        'busy_P':busy_P,
        'num_of_busy':num_of_busy,
    }
    return render(request, 'joylar.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def joy_detail(request, pk):
    change_posts_status()
    change_order_status()
    change_history()
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
    change_history()
    places = request.user.place_set.all()
    places_count = places.count()

    free_places = places.filter(busy="Bo'sh")
    busy_places = places.filter(busy="Band")

    free_places_count = free_places.count()
    busy_places_count = busy_places.count()
    
    orders = Order.objects.filter(place__owner = request.user)

    active_count = orders.filter(status='Active').count()
    active = orders.filter(status='Active')
    history = orders.filter(status='NotActive')
    #paginator
    p = Paginator(free_places, 1)
    page = request.GET.get('page')
    free_P = p.get_page(page)
    num_of_free = 'a' * free_P.paginator.num_pages

    
    p2 = Paginator(busy_places, 1)
    page2 = request.GET.get('page2')
    busy_P = p.get_page(page2)
    num_of_busy = 'a' * busy_P.paginator.num_pages

    p3 = Paginator(active, 1)
    page3 = request.GET.get('page3')
    active_P = p.get_page(page3)
    num_of_active = 'a' * active_P.paginator.num_pages
    
    
    p4 = Paginator(history, 1)
    page4 = request.GET.get('page4')
    history_P = p.get_page(page4)
    num_of_history = 'a' * history_P.paginator.num_pages
    # endpaginator

    context = {
        'places_count': places_count,
        'free_places_count': free_places_count,
        'busy_places_count': busy_places_count,
        'active_count': active_count,
        'free_P':free_P,
        'num_of_free':num_of_free,
        'busy_P':busy_P,
        'num_of_busy':num_of_busy,
        'active_P':active_P,
        'num_of_active':num_of_active,
        'history_P':history_P,
        'num_of_history':num_of_history,
    }
    return render(request, 'user-place.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['owner', 'admin'])
def detailPage(request, pk):

    change_posts_status()
    change_order_status()
    change_history()

    place = get_object_or_404(Place, id=pk)
    orders = place.order_set.all()

    active = orders.filter(status='Active')
    not_active = orders.filter(status='NotActive')

    #paginator
    p1 = Paginator(active, 1)
    page1 = request.GET.get('page1')
    active_P = p1.get_page(page1)
    num_of_active = 'a' * active_P.paginator.num_pages

    p2 = Paginator(not_active, 1)
    page2 = request.GET.get('page2')
    not_active_P = p2.get_page(page2)
    num_of_not_active = 'a' * not_active_P.paginator.num_pages

    context = {
        'place': place,
        'orders': orders,
        'active': active,
        'not_active': not_active,
        'active_P':active_P,
        'num_of_active':num_of_active,
        'not_active_P':not_active_P,
        'num_of_not_active':num_of_not_active
    }
    return render(request, 'user_detail.html', context)