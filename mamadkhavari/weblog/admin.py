from django.contrib import admin
from . import models

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','created_data', 'status')
    #hamin mire tu bakhshe post ha tuye admin panel neshun mide ke ina chian
    #typ yaeni masalan neshun mide ke ok ye table mishe shabihe table ke ina mishan sotun hash

    list_filter = ('title', 'author' ,'created_data','status') #in neshon mide tu panel che search boxi dashte bashim o unja chejuri search konim
    #mitunim faghat title bezarim ya faghat ye chi dige
    #daste khode adame
    search_fields = ('title',)



admin.site.register(models.Post, PostAdmin)
