from django.contrib import admin
from website_app.models import coffee,booktable


class CoffeeAdmin(admin.ModelAdmin):
    list_display=['id','name','price','cat','is_active']
    list_filter=['cat','is_active']

# Register your models here.
admin.site.register(coffee,CoffeeAdmin) 

class booktableAdmin(admin.ModelAdmin):
    list_display=['name','email','date','time','people','message','status']

admin.site.register(booktable,booktableAdmin)