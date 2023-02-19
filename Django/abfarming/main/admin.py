from django.contrib import admin
from main.models import farmer
from django.contrib.auth.admin import UserAdmin

class AccountAdmin(UserAdmin):
    list_display = ( 'fname','lname','phone_number','last_login','username','email','is_active','location')
    search_fields = ( 'phone_number','email','fname','lname')
    readonly_fields = ('last_login',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(farmer,AccountAdmin)

