from django.conf.urls import patterns, include, url


urlpatterns = patterns('map.views',
    url(r'^$', 'my_places', name='map_home'),
    url(r'^(?P<pk>\d+)/$', 'place_view', name='map_place_view'),
    url(r'^(?P<place_pk>\d+)/sensors$', 'list_sensors', name='list_sensors'),
    url(r'^(?P<place_pk>\d+)/sensors/new$', 'create_sensor', name='create_sensor'),
    url(r'^(?P<place_pk>\d+)/sensors/(?P<sensor_pk>\d+)$', 'edit_sensor', name='edit_sensor'),
    url(r'^(?P<place_pk>\d+)/sensors/(?P<sensor_pk>\d+)/delete$', 'delete_sensor', name='delete_sensor'),
    url(r'^(?P<place>\d+)/rules/', include('rule_engine.urls')),
    url(r'^(?P<place_pk>\d+)/history/(?P<int_date>\d+)/$', 'map_history', name='map_history'),

)
