from django.contrib import admin
from .models import Webinar, Workshop, Course, DFYTool, RetainerPlan, AcceleratorPackage


@admin.register(Webinar)
class WebinarAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'price', 'is_active')
    search_fields = ('title',)
    list_filter = ('date', 'is_active')


@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'schedule', 'price')
    search_fields = ('title',)
    list_filter = ('level', 'schedule')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'price', 'certificate')
    search_fields = ('title',)
    list_filter = ('certificate',)


@admin.register(DFYTool)
class DFYToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    search_fields = ('name', 'category')
    list_filter = ('category',)


@admin.register(RetainerPlan)
class RetainerPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'monthly_fee')
    search_fields = ('name',)


@admin.register(AcceleratorPackage)
class AcceleratorPackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'price')
    search_fields = ('name',)
