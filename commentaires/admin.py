from django.contrib import admin
from .models import Comment

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('publication','auteur', 'content','created_date' )
    search_fields = ('content','auteur_username')
