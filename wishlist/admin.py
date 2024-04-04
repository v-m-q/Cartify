from django.contrib import admin
from wishlist.models import Wishlist

class ReadOnlyModelAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    # Allow viewing objects but not actually changing them
    def has_change_permission(self, request, obj=None):
        if request.method not in ('GET', 'HEAD'):
            return False
        return super().has_change_permission(request, obj)


# Register your models here.
admin.site.register(Wishlist, ReadOnlyModelAdmin)