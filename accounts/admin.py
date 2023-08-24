from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, UserProfile, BillingAddress
from django.utils.html import format_html


# Register your models here.
class BillingAddressInline(admin.TabularInline):
    model = BillingAddress
    extra = 1


class AccountAdmin(UserAdmin):
    list_display = ['email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active']
    list_display_links = ['email', 'first_name', 'last_name']
    readonly_fields = ['last_login', 'date_joined']
    ordering = ['-date_joined',]

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    inlines = [BillingAddressInline]


class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))
    thumbnail.short_description = 'Profile Picture'
    list_display = ('thumbnail', 'user', 'city', 'state', 'country')


class BillingAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_full_name', 'phone_number', 'city', 'state', 'country')
    list_filter = ('user', 'city', 'state', 'country')
    search_fields = ('user__email', 'first_name', 'last_name', 'phone_number', 'city', 'state', 'country')
    
    def get_full_name(self, obj):
        return obj.get_full_name()
    get_full_name.short_description = 'Full Name'


admin.site.register(Account, AccountAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(BillingAddress, BillingAddressAdmin)