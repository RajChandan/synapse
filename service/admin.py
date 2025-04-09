from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Webinar, Workshop, Course, DFYTool, RetainerPlan, AcceleratorPackage

admin.site.register(Webinar)
admin.site.register(Workshop)
admin.site.register(Course)
admin.site.register(DFYTool)
admin.site.register(RetainerPlan)
admin.site.register(AcceleratorPackage)
