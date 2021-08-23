from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

#Custom Manager
class ActiveChatManager(models.Manager):
	def get_queryset(self):
		return super(ActiveChatManager,
					self).get_queryset()\
						.filter(status='active')

class ArchivedManager(models.Manager):
	def get_queryset(self):
		return super(ArchivedManager,
					self).get_queryset()\
						.filter(status='archived')

class ChatBox(models.Model):
	STATUS_CHOICES = (
		('active', 'Active'),
		('archived', 'Archived'),
	)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
	objects = models.Manager()
	active = ActiveChatManager()
	archived = ArchivedManager()

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return f"Chatbox created at {self.created}"

	def get_absolute_url(self):
		return reverse('teleusap:chat_box',
						args=[self.updated.year, self.id])

class Message(models.Model):
	chatbox = models.ForeignKey(ChatBox, on_delete=models.CASCADE)
	messager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messager')
	receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
	message = models.CharField(max_length=1000)
	file = models.FileField(blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('created',)

	def __str__(self):
		return f"message from {self.messager} to {self.receiver} at {self.created}"