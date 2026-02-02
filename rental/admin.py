from django.contrib import admin
from .models import Equipment, RentalRequest

class RentalRequestAdmin(admin.ModelAdmin):
    list_display=('user','equipment','total_price','status') #! Show these fields as columns in admin list page. 
    list_editable = ('status',)

    def save_model(self, request, obj, form, change):
        if obj.status == "Approved":
            obj.equipment.is_available = False
            obj.equipment.save()
        super().save_model(request,obj,form,change)    #! Finally save the RentalRequest normally. 
        #! When admin approves a rental request, this code automatically makes the equipment unavailable and then saves the request.

admin.site.register(Equipment)
admin.site.register(RentalRequest,RentalRequestAdmin)