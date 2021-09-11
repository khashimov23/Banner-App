from banner.models import Order, Place, Place_owner, Tadbirkor
from django.shortcuts import render, redirect

from banner.forms import OrderForm, OwnerForm, TadbirkorForm, JoyForm
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from django.urls import reverse


@login_required(login_url='login')
def createOwner(request):
    form = OwnerForm()

    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_joy')

    context = {'form': form}
    return render(request, 'forms/owner_form.html', context)



@login_required(login_url='login')
def updateOwner(request, pk):
    egasi = Place_owner.objects.get(id=pk)
    form = OwnerForm(instance=egasi)

    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=egasi)
        if form.is_valid():
            form.save()
            return redirect('place')

    context = {'form': form}
    return render(request, 'forms/owner_form.html', context)



@login_required(login_url='login')
def deleteOwner(request, pk):
    egasi = Place_owner.objects.get(id=pk)
    if request.method == 'POST':
        egasi.delete()
        return redirect('place')

    context = {'egasi':egasi}
    return render(request, 'forms/owner_delete.html', context)







@login_required(login_url='login')
def createTadbirkor(request):
    form = TadbirkorForm()

    if request.method == 'POST':
        form = TadbirkorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tadbirkor')

    context = {'form': form}
    return render(request, 'forms/tadbirkor_form.html', context)



@login_required(login_url='login')
def updateTadbirkor(request, pk):
    tadbirkor = Tadbirkor.objects.get(id=pk)
    form = TadbirkorForm(instance=tadbirkor)

    if request.method == 'POST':
        form = TadbirkorForm(request.POST, instance=tadbirkor)
        if form.is_valid():
            form.save()
            return redirect('tadbirkor')

    context = {'form': form}
    return render(request, 'forms/tadbirkor_form.html', context)



@login_required(login_url='login')
def deleteTadbirkor(request, pk):
    tadbirkor = Tadbirkor.objects.get(id=pk)
    if request.method == 'POST':
        tadbirkor.delete()
        return redirect('tadbirkor')

    context = {'tadbirkor':tadbirkor}
    return render(request, 'forms/tadbirkor_delete.html', context)







@login_required(login_url='login')
def createJoy(request):
    form = JoyForm()

    if request.method == 'POST':
        
        form = JoyForm(request.POST)
        if form.is_valid():
            joy = form.save(commit=False)
            joy.owner = request.user
            joy.save()
            return redirect('places')

    context = {'form': form}
    return render(request, 'forms/joy_form.html', context)


@login_required(login_url='login')
def updateJoy(request, pk):
    joy = Place.objects.get(id=pk)
    form = JoyForm(instance=joy)

    if request.method == 'POST':
        form = JoyForm(request.POST, instance=joy)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('place'))

    context = {'form': form}
    return render(request, 'forms/joy_form.html', context)


@login_required(login_url='login')
def deleteJoy(request, pk):
    joy = Place.objects.get(id=pk)
    if request.method == 'POST':
        joy.delete()
        return redirect('/')

    context = {'joy':joy}
    return render(request, 'forms/joy_delete.html', context)







@login_required(login_url='login')
def createOrder(request):
    form = OrderForm()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders')

    context = {'form': form}
    return render(request, 'forms/order_form.html', context)


@login_required(login_url='login')
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders')

    context = {'form': form}
    return render(request, 'forms/order_form.html', context)


@login_required(login_url='login')
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('orders')

    context = {'order':order}
    return render(request, 'forms/delete_order.html', context)

