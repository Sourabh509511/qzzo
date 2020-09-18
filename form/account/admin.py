from django.contrib import admin
from django.contrib.auth import get_user_model
from .forms import UserAdminChangeForm,UserAdminCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
User=get_user_model()

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('Email','admin' )
    list_filter = ('admin','staff')
    fieldsets = (
        (None, {'fields': ('Email', 'password')}),
        ('Other Info', {'fields': ('Image','First_name',"Last_name","Age","Unique_id")}),
        ('Permissions', {'fields': ('admin','staff','active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('Image','First_name',"Last_name","Age","Unique_id",'Email', 'password1', 'password2','admin','staff','active')}
        ),
    )
    search_fields = ('Email',)
    ordering = ('Email',)
    filter_horizontal = ()

admin.site.register(User,UserAdmin)