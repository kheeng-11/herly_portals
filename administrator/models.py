from django.db import models

class admin(models.Model):
	admin_usermail = models.CharField(max_length=255)
	admin_fname = models.CharField(max_length=255)
	admin_othernames = models.CharField(max_length=255)
	admin_password = models.CharField(max_length=255)

	def __str__(self):
		return self.admin_usermail

class section(models.Model):
	section_name = models.CharField(max_length=255)
	section_added_on = models.CharField(max_length=255)

	def __str__(self):
		return self.section_name
