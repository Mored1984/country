#/usr/bin/env python
import requests		# plug to get data from websites (URLs)
import sys			# To deal with operation system
import os			# To deal with operation system

# workon country
sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

# Import Country
from main.models import Country
response = requests.get('https://restcountries.eu/rest/v1/all')

# Print response
response_dict=response.json()		# json already installed with requests plug

# Print response_dict
for data in response_dict:
	print data['name']
	print '-----------------'
	country, created = Country.objects.get_or_create(name=data['name'])
	print created
	country.capital = data['capital']
	country.population = data['population']
	country.save()