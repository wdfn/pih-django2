from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from pih import settings
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pih.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'pih.views.home', name='home'),

    url(r'^about-us\.html/$', 'pih.views.aboutus', name='aboutus'),
	url(r'^blog\.html/$', 'pih.views.blog', name='blog'),
	url(r'^contact-us\.html/$', 'pih.views.contactus', name='contactus'),

#admin system
    url(r'^admin/', include(admin.site.urls)),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

