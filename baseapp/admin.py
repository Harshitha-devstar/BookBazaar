from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from .models import User, Category, Book

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'name','phone')}),
        ('Permissions', {'fields':(
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )}),

    )
    add_fieldsets = (
        (
        None, 
            {
                'classes': ('wide',),
                'fields':('email','name','phone', 'password1', 'password2')
            }
        ),
    )

    list_display = ('email', 'name', 'is_staff', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'books_sold', 'books_bought')
    search_fields = ('email', )
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions')
    

admin.site.register(User, UserAdmin)


# registering Books and Genre model in admin

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug' : ('name',)}
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=[
        'name',
        'slug',
        'price',
        'available',
        'created',
        'updated',
        'condition',
    ]
    list_filter = ['available', 'created', 'updated', 'condition']
    list_editable = ['price', 'available', 'condition']
    prepopulated_fields = {'slug':('name',)}
