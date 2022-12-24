from django.contrib import admin
from .models import Users, Companies, Houses


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'email', 'phone')
    list_display_links = ('name', 'email')
    search_fields = ('name',)


admin.site.register(Users, UserAdmin)
admin.site.register(Companies)
admin.site.register(Houses)
