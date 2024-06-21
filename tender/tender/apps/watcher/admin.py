from django.contrib import admin
from .models import Region, Unit, Category, Tender, Vender, Addres, Client, Partner, Application, Status
# Register your models here.

admin.site.register(Region)
admin.site.register(Category)
admin.site.register(Tender)
#admin.site.register(Addres)

class AddresAdmin(admin.ModelAdmin):
    list_display = ('idaddress', 'addresscol')

admin.site.register(Addres, AddresAdmin)

admin.site.register(Client)
admin.site.register(Partner)
admin.site.register(Status)  