from banner.models import Order, Place, Place_owner, Tadbirkor
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    orders = Order.objects.all()
    egasi = Place_owner.objects.all()
    places = Place.objects.all()

    egalari = []
    for eg in egasi:
        
        places_count = eg.place_set.all().count()
        dt = {
            "id":eg.id,
            "name":eg.name,
            "phone":eg.phone,
            "places_count":places_count
        }
        egalari.append(dt)

   
    places = Place.objects.all()
    free_places = places.filter(busy="Bo'sh").count()
    busy_places = places.filter(busy="Band").count()

    total_places = places.count()
    total_orders = orders.count()
    total_owners = egasi.count()
    total_tadbirkor = Tadbirkor.objects.all().count()

    active = orders.filter(status='active')

    context = {
        'orders': orders,
        'places': places,
        'egalari': egalari,
        'free_places': free_places,
        'busy_places': busy_places,
        'total_places': total_places,
        'total_orders': total_orders,
        'total_owners': total_owners,
        'total_tadbirkor': total_tadbirkor,
        'active': active,
    }

    return render(request, 'dashboard.html', context)


@login_required(login_url='login')
def order(request):
    
    orders = Order.objects.all()
    orders_count = orders.count()

    context = {'orders': orders, 
    'orders_count': orders_count}
    return render(request, 'orders.html', context)



@login_required(login_url='login')
def tadbirkor(request):
    tadbirkorlar = Tadbirkor.objects.all()

    tadbirkorlar_soni = Tadbirkor.objects.all().count()


    return render(request, 'tadbirkor.html', {'tadbirkorlar': tadbirkorlar, 'tadbirkorlar_soni': tadbirkorlar_soni})


@login_required(login_url='login')
def tadbirkor_detail(request, pk):
    tadbirkor = Tadbirkor.objects.get(id=pk)

    orders = tadbirkor.order_set.all()

    orders_count = tadbirkor.order_set.all().count()

    context = {
    'tadbirkor': tadbirkor, 
    'orders': orders,
    'orders_count': orders_count}
    return render(request, 'tad_detail.html', context)



@login_required(login_url='login')
def place(request):
    places = Place.objects.all()
    free_places = places.filter(busy="Bo'sh").count()
    busy_places = places.filter(busy="Band").count()
    total_places = places.count()


    egalari = Place_owner.objects.all()
    total_owners = egalari.count()

    egasi = []
    for ega in egalari:
        
        places_count = ega.place_set.all().count()
        dt = {
            "id":ega.id,
            "name":ega.name,
            "phone":ega.phone,
            "places_count":places_count
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
def place_detail(request, pk):
    egasi = Place_owner.objects.get(id=pk)
    places = egasi.place_set.all()

    places_count = egasi.place_set.all().count()

    place = Place.objects.get(id=pk)
    orders = place.order_set.all().count()

    context = {
        'egasi': egasi, 
        'orders': orders, 
        'places': places,
        'places_count': places_count,
    }
    return render(request, 'owner_detail.html', context)







def joylar(request):
    places = Place.objects.all()
    egasi = Place_owner.objects.all()

    free_places = places.filter(busy="Bo'sh")
    busy_places = places.filter(busy="Band")

    free_places_count = places.filter(busy="Bo'sh").count()
    busy_places_count = places.filter(busy="Band").count()
    total_places_count = places.count()


    context = {
        'places': places,
        'egasi':egasi,

        'free_places': free_places,
        'busy_places': busy_places,

        'free_places_count': free_places_count,
        'busy_places_count': busy_places_count,
        'total_places_count': total_places_count,
    }
    return render(request, 'joylar.html', context)







def joy_detail(request, pk):

    place = Place.objects.get(id=pk)

    orders = place.order_set.all()

    context = {
        'place': place,
        'orders': orders,
    }
    return render(request, 'joy_detail.html', context)










