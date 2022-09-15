from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from api.models import Users,Books
# Register your models here.

class CustonAdmin(UserAdmin):
    list_display = ('email','date_joined','last_login','is_admin','is_staff')
    search_fields = ('email',)
    readonly_fields = ('id','date_joined','last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(Users,CustonAdmin)

admin.site.register(Books)