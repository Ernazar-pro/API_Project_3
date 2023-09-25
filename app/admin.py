from django.contrib import admin
from .models import Blog, Client, Sponsor

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname')
    list_display_links = ('id', 'fullname')

@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')