from django.contrib import admin
from myapp.models import Contact,Blogs

# Register your models here.

admin.site.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['id','name','email','phoneNumber','description']

admin.site.register(Blogs)




# @admin.register(Blog)
# class BlogAdmin(admin.ModelAdmin):
#     list_display = ['id','image','title','description','date']