from django.shortcuts import render, redirect    # add redirect function to link to new url
from models import Country, Review
from django.http import HttpResponse
from forms import CreateCountryForm, CreateUserForm, LoginForm, CreateReviewForm, EditReviewForm	# To import class "CreateCountryForm"
# Create your views here.
from django.contrib.auth.decorators import login_required	# to make only loged in user to view this page 
from django.contrib.admin.views.decorators import staff_member_required	# only superuser can view this page

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from datetime import datetime


def countrylist(request):
	context={}
	countries=Country.objects.all()			# .obeject.all() to inherate from the class 
	# or
	# context['country_list']=Country.objects.all()
	context['country_list']=countries
	print context
	return render(request,'country_list.html',context)

def countrydetail(request,pk):
	context={}
	country=Country.objects.get(pk=pk)
	context['country']=country

	# return HttpResponse(country)


	# Create Review Form
	context['form']=CreateReviewForm()

	if request.method == 'POST':
		form=CreateReviewForm(request.POST)
		context['form']=form
		if form.is_valid():
			review=form.save(commit=False)
			review.date=datetime.now()
			review.country=country
			review.user=request.user
			review.save()
			return redirect('/countrylist/')

	return render(request, 'country_detail.html', context)

@login_required
def createcountry(request):		# "creatcountry" is only name
	context={}
	context['form']=CreateCountryForm()

	# Add to database
	if request.method=='POST':
		# Make sure from is valid
		form = CreateCountryForm(request.POST, request.FILES)
		context['form']=form 	# when it's invalid let return on same url with same what customer already has entered

		if form.is_valid():
			# Save the form in database
			form.save()
			return render(request,'countrycreated.html',context)


	return render(request,'createcountry.html',context)

def sign_up(request):
	context={}							# make context empty
	context['form']=CreateUserForm()	# Copy CreateUserForm to form inside context

	if request.method=='POST':			# only work when user submit some input to website (2nd time)
		form=CreateUserForm(request.POST)	# copy form (2nd website or POST is true) to form (variable)
		context['formn']=form 				# copy the form variable to our context

		if form.is_valid():
			username=form.cleaned_data['username']
			email=form.cleaned_data['email']
			password=form.cleaned_data['password1']

			new_user=User.objects.create_user(username=username, password=password, email=email)
			new_user.save()

			# To let the user automatic login after succeful sign Up
			auth_user=authenticate(username=username, password=password, email=email)	# Check username and password from database then copy to auth_user
			login(request, auth_user)

			return redirect('/countrylist/')	# Redirect to URL after automatic login

	return render(request,'sign_up.html',context)	# Only will work when first time open the URL (GET)


def sign_in(request):
	context={}							# make context empty
	context['form']=LoginForm()	# Copy CreateUserForm to form inside context

	if request.method=='POST':			# only work when user submit some input to website (2nd time)
		form=LoginForm(request.POST)	# copy form (2nd website or POST is true) to form (variable)
		context['form']=form 				# copy the form variable to our context

		if form.is_valid():
			username=form.cleaned_data['username']
			password=form.cleaned_data['password2']

			try:		# Let my code be smart by take action even if the user didn't do this I will take another action
				# After I bring the username and password I need to authenticate
				auth_user=authenticate(username=username, password=password)	# Check username and password from database then copy to auth_user
				login(request, auth_user)
				return redirect('/countrylist/')
			except Exception, e:
				return HttpResponse('Wrong username or password !! please <a href="/signin/">!!!Try again !!!</a>')

	return render(request,'sign_in.html',context)	# Only will work when first time open the URL (GET)


def sign_out(request):
	logout(request)
	return redirect('/countrylist/')


@login_required
def editreview(request, pk):
	context={}							# make context empty
	review=Review.objects.get(pk=pk)

	if request.user == review.user:
		context['review']=review
		form=EditReviewForm(request.POST or None, instance=review)

		context['form']=form

		if form.is_valid():
			form.save()
			return redirect('/countrylist/')
		else:
			return HttpResponse('Go Away Hacker !!')
	return render(request,'editreview.html',context)


@login_required
def deletereview(request,pk):
	review=Review.objects.get(pk=pk)

	if request.user==review.user:
		review.delete()
	return redirect('/countrylist/')