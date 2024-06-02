from django.contrib import admin

from .models import Environment, Solution, Computer

# Register your models here.

@admin.register(Environment)
class EnvironmentAdmin(admin.ModelAdmin):
    list_display = ['environment_name','environment_description', 'created_at', 'updated_at']



@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ['solution_name', 'solution_description', 'created_at', 'updated_at']



@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    list_display = ['computer_name', 'computer_ip', 'solution','environment', 'created_at', 'updated_at']
