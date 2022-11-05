from django.contrib import admin

# Register your models here.
from .models import BotUsers,Image
admin.site.register(Image)
@admin.register(BotUsers)
class BotUsersAdmin(admin.ModelAdmin):
    list_display = ['full_name','telegram_id','language']
    search_fields = ['full_name','telegram_id','language']
    list_filter = ['language']
    list_per_page =10
