from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Broadcast_app.views.index'),
    url(r'^login$', 'Broadcast_app.views.login_view'),
    url(r'^logout$', 'Broadcast_app.views.logout_view'),
    url(r'^signup$', 'Broadcast_app.views.signup'),
    url(r'^broadcasts$', 'Broadcast_app.views.public'),
    url(r'^submit$', 'Broadcast_app.views.submit'),
    url(r'^users/$', 'Broadcast_app.views.users'),
    url(r'^users/(?P<username>\w{0,30})/$', 'Broadcast_app.views.users'),
    url(r'^follow$', 'Broadcast_app.views.follow'),
    # url(r'^broadcast/', include('broadcast.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )
