from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserAccountCreationForm, UserAccountChangeForm
from .models import UserAccount

# Register your models here.

class UserAccountAdmin(UserAdmin):
    add_form = UserAccountCreationForm
    form = UserAccountChangeForm
    model = UserAccount
    list_display = ['username', 'email', 'joining_date', 'is_staff', 'date_of_birth']

admin.site.register(UserAccount, UserAccountAdmin)
