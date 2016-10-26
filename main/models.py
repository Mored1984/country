from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Country(models.Model):	# must class start with capital latter
	name=models.CharField(max_length=255)	#CharField is command in dJango with max lenght (limited to the number I added)
	capital=models.CharField(max_length=255,null=True,blank=True) # null is to allow store null inside the database & blank to allow the user to let the input empty
	population=models.IntegerField(null=True,blank=True)
	flag=models.ImageField(null=True,blank=True,upload_to='flags')

	def __unicode__(self):	# to sort the column the database by name
		return self.name	# only text (if column is number will give error) 
		# return '%s' % self.id	# to sort even number


# Create new form for Reviews only for certain country
class Review(models.Model):	# Automatic generate form created from Model
	title=models.CharField(max_length=255)	# CharField for string input (must put max length)
	content=models.TextField()				# Infinit text
	date=models.DateTimeField(auto_now_add=True)	# Computer will add this automatically
	country=models.ForeignKey(Country)		# Relationship many to one also we called "ForeignKey"
	user=models.ForeignKey(User)			# To use the User we must first import it {Line 2}
	def __unicode__(self):
		return self.title
