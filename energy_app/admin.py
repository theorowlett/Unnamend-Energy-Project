from django.contrib import admin
from .models import CustomUser,Data,Annual_Data

# Register your models here.

class AnnualDataInline(admin.TabularInline):
    model = Annual_Data

class DataAdmin(admin.ModelAdmin):
    inlines = [AnnualDataInline]
    class Meta:
        model = Data

admin.site.register(CustomUser)
admin.site.register(Data, DataAdmin)