from django.contrib import admin

# Register your models here.
from .models import MobilePhone, Manufacturer


class MobilePhoneAdmin(admin.ModelAdmin):
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(MobilePhoneAdmin, self).save_model(request, obj, form, change)


admin.site.register(MobilePhone, MobilePhoneAdmin)
admin.site.register(Manufacturer)