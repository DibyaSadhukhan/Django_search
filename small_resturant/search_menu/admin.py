from django.contrib import admin
from search_menu.models import resturant_details,menu_details,menu_items,search_history
# Register your models here.
admin.site.register(resturant_details)
admin.site.register(menu_details)
admin.site.register(menu_items)
admin.site.register(search_history)