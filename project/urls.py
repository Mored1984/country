from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^countrylist/$', 'main.views.countrylist'),		# ^ start with name & $ to end with the name
 # url(r'contactus',''),	# I can write www.website.com/dsafdsafconatctuskdsajhkdja  
 	url(r'^country/(?P<pk>\d+)/$','main.views.countrydetail'),
 	url(r'^createcountry/$','main.views.createcountry'),
 	url(r'^signup/$','main.views.sign_up'),
 	url(r'^signin/$','main.views.sign_in'),
 	url(r'^signout/$','main.views.sign_out'),
 	url(r'^editreview/(?P<pk>\d+)/$','main.views.editreview'),
 	url(r'^deletereview/(?P<pk>\d+)/$','main.views.deletereview'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
