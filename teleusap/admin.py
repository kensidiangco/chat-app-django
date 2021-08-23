from django.contrib import admin
from .models import Message, ChatBox

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
	list_display = ('messager', 'created')
	list_filter = ('messager', 'receiver', 'created')
	search_fields = ('messager', 'receiver', 'message')

@admin.register(ChatBox)
class ChatBox(admin.ModelAdmin):
	list_filter = ('created', 'status')
	search_fields = ('status',)
	ordering = ('status', 'created')