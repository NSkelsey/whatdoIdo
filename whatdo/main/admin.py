from django.contrib import admin
from whatdo.main.models import Activity, Catergory

class ActivityAdmin(admin.ModelAdmin):
    pass
admin.site.register(Activity, ActivityAdmin)

class CatergoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Catergory, CatergoryAdmin)


