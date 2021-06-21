from django.contrib import admin
# from .models import related models


# Register your models here.
admin.site.register(CarMake)
admin.site.register(CarModdel)
# CarModelInline class
class CarModelInline(CarModel.CarMake):
    model = CarModel 
    extra = 5
# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']
    inlines = [CarModelInline]
# CarMakeAdmin class with CarModelInline

# Register models here