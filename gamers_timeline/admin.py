from django.contrib import admin
from .models import Thread,Comment,Anchor


@admin.register(Thread)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class EntryAdmin(admin.ModelAdmin):
    pass

@admin.register(Anchor)
class UserAdmin(admin.ModelAdmin):
    pass
