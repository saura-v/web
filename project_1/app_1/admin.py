from django.contrib import admin
from .models import Student
# Register your models here.


# admin.site.register(Student)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','age','email','address']
    # this is use to display the name age email and all other datas
    list_display_links=['email']
    # this is use to open a link through email only 
    list_filter=['name','age']
    # this is use to filter that data from name 

    list_per_page=2
    # this will create from one page to another page 

    search_fields=['name']
    # ordering=['id']
    ordering=['-id']

    
