from django import forms
from main.models import Country, Review

class CreateCountryForm(forms.ModelForm):	# CreateCountryForm is only name of class it's smart form ".ModelForm"
	class Meta:
		model=Country
		fields='__all__'


class CreateUserForm(forms.Form):
	username=forms.CharField(max_length=30)	# CharField it's mean string input
	password1=forms.CharField(max_length=30,widget=forms.PasswordInput())	# widget=forms.PasswordInput() to let the password display as ******
	email=forms.EmailField(required=False)		# EmailField contain all properties for enter email roles, required=false to make this opitional


class LoginForm(forms.Form):
	username=forms.CharField(max_length=30)
	password2=forms.CharField(max_length=30,label='Password',widget=forms.PasswordInput())	# label='####' to show the #### for user not the variable


class CreateReviewForm(forms.ModelForm):
	class Meta:
		model=Review
		exclude=('date','country','user',)

class EditReviewForm(forms.ModelForm):
	class Meta:
		model=Review
		exclude=('date','country','user',)