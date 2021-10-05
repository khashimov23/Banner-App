from django import forms
from django.http.response import HttpResponse
from banner.models import Order, Place, Place_owner, Tadbirkor
from django.shortcuts import render, redirect, get_object_or_404

from banner.forms import OrderForm, TadbirkorForm, JoyForm, OwnerForm
from django.contrib.auth.decorators import login_required

from banner.decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib import messages




@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
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
@allowed_users(allowed_roles=['admin'])
def updateOwner(request, pk):
    if request.user.id == pk:
        egasi = Place_owner.objects.get(id=pk)
        form = OwnerForm(instance=egasi)

        if request.method == 'POST':
            form = OwnerForm(request.POST, instance=egasi)
            if form.is_valid():
                form.save()
                return redirect('/')

        context = {'form': form}
        return render(request, 'forms/owner_form.html', context)
    else:
        return HttpResponse("Sizga bu sahifaga kirish mumkin emas!")





#DELETE
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOwner(request, pk):
    egasi = Place_owner.objects.get(id=pk)
    if request.method == 'POST':
        egasi.delete()
        return redirect('/')
        
    context = {'item':egasi}
    return render(request, 'delete_owner.html', context)





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





#DELETE
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteTadbirkor(request, pk):
    tadbirkor = Tadbirkor.objects.get(id=pk)
    if request.method == 'POST':
        tadbirkor.delete()
        return redirect('/')
        
    context = {'item':tadbirkor}
    return render(request, 'delete_tadbirkor.html', context)










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
    joylar = Place.objects.filter(owner=request.user)
    joy = Place.objects.get(id=pk)

    if joylar.filter(id=pk).count()>0:

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
    else:
        return HttpResponse("Sizga bu sahifaga kirish mumkin emas!")


#DELETE
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteJoy(request, pk):
    joy = Place.objects.get(id=pk)
    if request.method == 'POST':
        joy.delete()
        return redirect('joylar')
        
    context = {'joy':joy}
    return render(request, 'forms/delete_joy.html', context)














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
    return render(request, 'forms/update_order.html', context)


@login_required(login_url='login')
def deleteOrder(request, pk):
    order = get_object_or_404(Order, id=pk)
    order.delete()
    return redirect('orders')





#DELETE
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('orders')
        
    context = {'item':order}
    return render(request, 'forms/delete_order.html', context)
