from django.contrib import admin
from .models import teacher, asset
from .models import Requests
from .models import Overdue
from .models import Repaired




# Register your models here.
class teacherAdmin(admin. ModelAdmin):
    list_display = ('Name', 'Area',)
admin.site.register(teacher, teacherAdmin)

class assetAdmin(admin.ModelAdmin):
    fields = ['name', 'Qrcode', 'description', 'category', 'image', 'admin_photo',]
   
    list_display = [
        'admin_photo',
        'name',
        'Qrcode',
        'description',
        'category',
        
    ]
    
    list_filter = [
        'name',
        'category',
       
       
    ]
    list_display_links=[
        'name',
        'category'
    ]
   
    
    readonly_fields = ('admin_photo',)
    
admin.site.site_header = 'Management Dashboard'
admin.site.register(asset, assetAdmin)

class OverdueInline(admin.StackedInline):
    model = Overdue
    extra = 0
    fields = ['sendby', 'assetname', 'assetid']
class RepairedInline(admin.StackedInline):
    model = Repaired
    extra = 0
    fields = ['sendby', 'assetname', 'assetid']
    inlines = [OverdueInline]
class RequestsAdmin(admin.ModelAdmin):
    inlines = [RepairedInline, OverdueInline]
    list_display = ['sendby', 'assetname', 'assetid', 'status']
admin.site.register(Requests, RequestsAdmin)


