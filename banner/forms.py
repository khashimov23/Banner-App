from django import forms
from django.forms import widgets
from .models import Order, Tadbirkor, Place, Place_owner

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']






class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['tadbirkor', 'place', 'start_date', 'end_date', 'status']

        widgets = {
            'start_date': forms.TextInput(attrs={'type': 'date'}),
            'end_date': forms.TextInput(attrs={'type': 'date'}),
            'tadbirkor': forms.Select(attrs={'class':"form-control"}),
            'place': forms.Select(attrs={'class':"form-control"}), 
            'status': forms.Select(attrs={'class':"form-control"}),
        }

        labels = {
            'tadbirkor': _('Tadbirkor'),
            'place': _('Joy'),
            'start_date': _('Boshlanish sanasi'),
            'end_date': _('Tugash sanasi'),
            'status': _('Holati')
        }



class OwnerForm(forms.ModelForm):
    class Meta:
        model = Place_owner
        fields = ['name', 'phone']

        labels = {
            'name': _('Nomi'),
            'phone': _('Telefon'),
        }




class TadbirkorForm(forms.ModelForm):
    class Meta:
        model = Tadbirkor
        fields = ['name', 'phone', 'info']

        labels = {
            'name': _('Nomi'),
            'phone': _('Telefon'),
            'info': _('Tavsif'),
        }


    


class JoyForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = [ 'address', 'price', 'description', 'image', 'image2', 'image3', 'busy', 'start_date', 'end_date', 'current_post']

        widgets = {
            'current_post': forms.Select(attrs={'class':"form-control"}), 
            'busy': forms.Select(attrs={'class':"form-control"}), 
            'start_date': forms.TextInput(attrs={'type': 'date'}),
            'end_date': forms.TextInput(attrs={'type': 'date'}),
        }

        labels = {
            'address': _('Nomi'),
            'price': _('Telefon'),
            'description': _('Tavsif'),
            'image': _('Birinchi rasm'),
            'image2': _('Ikkinchi rasm'),
            'image3': _('Uchunchi rasm'),
            'busy': _('Holati'),
            'start_date': _('Boshlanish sanasi'),
            'end_date': _('Tugash sanasi'),
            'current_post': _("Bog'langan tadbirkor"),
        }




