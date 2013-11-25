from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 				'interface.views.index', 	name='home'),
    url(r'^tower$', 		'tower.views.index', 		name="tower"),
    url(r'^tower/roll$',	'tower.views.roll', 		name="roll"),
)
