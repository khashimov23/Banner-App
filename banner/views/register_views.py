from django.shortcuts import render, redirect
from banner.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()                        
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')

                messages.success(request, f'Yangi hisob {user} uchun yaratildi')

                return redirect('login')

        context = {'form':form}
        return render(request, 'register/register.html', context)



def loginPage(request):
    if request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Parol yoki foydalanuvchi nomi hato!')

        context = {}
        return render(request, 'register/login.html', context)



def logOutUser(request):
    logout(request)
    return redirect('login')

