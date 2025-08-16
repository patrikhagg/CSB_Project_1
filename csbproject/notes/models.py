from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=100, blank=True)

	def save(self, *args, **kwargs):
		if not self.name and self.user:
			self.name = self.user.username
		super().save(*args, **kwargs)

class Note(models.Model):
	account = models.ForeignKey(Account, on_delete=models.CASCADE)
	content = models.TextField()