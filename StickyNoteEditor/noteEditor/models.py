from django.contrib.auth.models import Permission, User
from django.db import models

class StickyNote(models.Model):
	user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
	noteHead = models.CharField(max_length=100)
	noteBody = models.CharField(max_length=500)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.noteHead
