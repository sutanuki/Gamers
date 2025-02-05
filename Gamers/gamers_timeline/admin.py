from django.contrib import admin
from .models import Thread,Comment,Anchor


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Anchor)
class AnchorAdmin(admin.ModelAdmin):
    pass
