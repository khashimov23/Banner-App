from django import forms
from banner.models import Order, Place, Place_owner, Tadbirkor
from django.shortcuts import render, redirect, get_object_or_404

from banner.forms import OrderForm, TadbirkorForm, JoyForm, OwnerForm
from django.contrib.auth.decorators import login_required

from django.contrib import messages




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
            return redirect('/')

    context = {'form': form}
    return render(request, 'forms/owner_form.html', context)



@login_required(login_url='login')
def deleteOwner(request, pk):
    egasi = Place_owner.objects.get(id=pk)
    egasi.delete()
    return redirect('/')




@login_required(login_url='login')
def createTadbirkor(request):
    form = TadbirkorForm()

    if request.method == 'POST':
        form = TadbirkorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_order')

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
            return redirect('create_order')

    context = {'form': form}
    return render(request, 'forms/tadbirkor_form.html', context)



@login_required(login_url='login')
def deleteTadbirkor(request, pk):
    tadbirkor = get_object_or_404(Tadbirkor, id=pk)
    tadbirkor.delete()
    return redirect('tadbirkor')







@login_required(login_url='login')
def createJoy(request):

    form = JoyForm()
    if request.method == 'POST':    
        
        form = JoyForm(request.POST, request.FILES)

        if form.is_valid():
            joy = form.save(commit=False)
            joy.owner = request.user
            joy.save()
            messages.success(request, 'Sizning joyingiz yaratildi')
            return redirect('user_page', pk=request.user.id)
        else:
            messages.error(request, 'Sizda hatolik yuz berdi')
            return redirect('user_page', pk=request.user.id)


    context = {'form': form}
    return render(request, 'forms/create_joy.html', context)


@login_required(login_url='login')
def updateJoy(request, pk):
    joy = get_object_or_404(Place, id=pk)
    form = JoyForm(instance=joy)

    if request.method == 'POST':
        joy.image = request.FILES["image"]
        joy.save()
        form = JoyForm(request.POST, instance=joy)
        if form.is_valid():
            form.save()
            return redirect('user_page', pk=request.user.id)

    context = {'form': form, 'joy': joy}
    return render(request, 'forms/update_joy.html', context)


@login_required(login_url='login')
def deleteJoy(request, pk):
    joy = get_object_or_404(Place, id=pk)
    joy.delete()
    return redirect('user_page', pk=request.user.id)















@login_required(login_url='login')
def createOrder(request):
    form = OrderForm()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Buyurtma amalga ochirildi.')
            return redirect('orders')

    context = {'form': form}
    return render(request, 'forms/order_form.html', context)


@login_required(login_url='login')
def updateOrder(request, pk):
    order = get_object_or_404(Order, id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, 'Buyurtma tahrirlandi.')
            return redirect('orders')

    context = {'form': form}
    return render(request, 'forms/order_form.html', context)


@login_required(login_url='login')
def deleteOrder(request, pk):
    order = get_object_or_404(Order, id=pk)
    order.delete()
    return redirect('orders')