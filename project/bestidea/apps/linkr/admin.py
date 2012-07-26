from bestidea.apps.linkr.models import Topic, Item
from django.contrib import admin


class TopicAdmin(admin.ModelAdmin):
    list_display=('id','name','modified','user')
    fieldsets = [
        (None,               {'fields': ['name','desc','user']}),
       
    ]
    save_on_top=True 

class ItemAdmin(admin.ModelAdmin):
  list_display=('id','url')
  fieldsets = [
        (None,               {'fields': ['url','desc','topics']}),
    
    ]
  save_on_top=True 
  list_filter = ['created']
  search_fields = ['desc']
  
admin.site.register(Topic,TopicAdmin)
admin.site.register(Item,ItemAdmin)