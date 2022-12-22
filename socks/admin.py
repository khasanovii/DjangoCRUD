from django.contrib import admin
from .models import GeeksModel
# Register your models here.
class GeeksModelAdmin(admin.ModelAdmin):
    title = ['title']
    description = ['description']
    def __str__(self):
        return self.title
admin.site.register(GeeksModel, GeeksModelAdmin)