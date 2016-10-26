from django.contrib import admin
from models import Country, Review			# U can write like
#from models import *						# So * will let all class imported

# Register your models here.

admin.site.register(Country)
admin.site.register(Review)