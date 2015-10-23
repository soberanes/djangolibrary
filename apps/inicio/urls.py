from django.conf.urls import include, url

urlpatterns = [

    url(r'^$', 'django.contrib.auth.views.login',
                    {'template_name':'inicio/index.html'}, name='login'),

    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login',
                    name='logout'),

]
