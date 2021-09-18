from django import forms
from django.forms import widgets
from .models import Order, Tadbirkor, Place, Place_owner

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm



class CreateUserForm(UserCreationForm):
    class Meta:
        model = Place_owner
        fields = ['username', 'phone', 'password1', 'password2']




class OwnerForm(forms.ModelForm):
    class Meta:
        model = Place_owner
        fields = ['username', 'phone']

        labels = {
            'username': _('Faydalanuvchining ismi'),
            'phone': _('Telefon'),
        }





class OrderForm(forms.ModelForm):
    
    def __init__(self,*args,**kwargs):
        super (OrderForm,self ).__init__(*args,**kwargs)
        self.fields['place'].queryset = Place.objects.filter(busy="Bo'sh")


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
        fields = ['address', 'price', 'description', 'image', 'image2', 'image3', 'busy', 'start_date', 'end_date', 'boglangan_tadbirkor']

        widgets = {
            'boglangan_tadbirkor': forms.TextInput(attrs={'class':"form-control", 'placeholder':'Nomini kiriting..'}), 
            'busy': forms.Select(attrs={'class':"form-control"}), 
            'start_date': forms.TextInput(attrs={'type': 'date'}),
            'end_date': forms.TextInput(attrs={'type': 'date'}),
            'image': forms.ClearableFileInput(),
            'image2': forms.ClearableFileInput(),
            'image3': forms.ClearableFileInput(),
            'address': forms.TextInput(attrs={'class':"form-control", 'placeholder': "ex: Andijon - Eski shahar "}),
            'price': forms.TextInput(attrs={'class':"form-control", 'placeholder': "ex: oyiga - 500.000 so'm"}),
            'description': forms.TextInput(attrs={'class':"form-control", 'placeholder': "ex: joyimizni batafsil rasmlarini ko'rishingiz mumkin."}),
        }

        labels = {
            'address': _('Manzili'),
            'price': _('Narxi'),
            'description': _('Tavsif'),
            'image': _('Birinchi rasm'),
            'image2': _('Ikkinchi rasm'),
            'image3': _('Uchunchi rasm'),
            'busy': _('Holati'),
            'start_date': _('Boshlanish sanasi'),
            'end_date': _('Tugash sanasi'),
            'boglangan_tadbirkor': _("Bog'langan tadbirkor"),
        }




