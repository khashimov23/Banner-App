from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class CustomUserAdmin(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone',)}),
    )

admin.site.register(Place_owner)
admin.site.register(Place)
admin.site.register(Tadbirkor)
admin.site.register(Order)