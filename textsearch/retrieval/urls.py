from django.urls import path, re_path

from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('query', views.text_query, name='text_query'),
	path('iquery', views.image_query, name='upload_query'),
	path('results', views.results, name='results'),
	path('show_image', views.show_image, name='show_image'),
	path('show_page', views.show_page, name='show_page'),
	path('project', views.about_project, name='about_project'),
	path('search', views.query, name='search'),
	re_path(r'^chome/(?P<cname>\w+)/$', views.collection_index, name='chome'),
	re_path(r'^mresults/(?P<page>\d)/$', views.mresults, name='mresults'),
	re_path(r'^view_results/(?P<page>\d)/(?P<pid>\d)/$', views.view_results, name='view_results'),
	re_path(r'^dresults/(?P<im_id>\d)/$', views.demo_results, name='dresults'),
	re_path(r'^redirect_/(?P<cname>\w+)/(?P<choice>\d)/$', views.redirect_query, name='redirect_'),
	]