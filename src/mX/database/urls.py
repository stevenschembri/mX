from django.conf.urls import url

from .views import ( DatabaseHomePageView, DatabaseCustomerView, DatabaseCustomerAddView, DatabaseCustomerDetailView,
	DatabaseAircraftView, DatabaseAircraftAddView, DatabaseAircraftDetailView
	)


urlpatterns = [
    url(r'^$', DatabaseHomePageView.as_view(), name='home'),
    url(r'^customer/$', DatabaseCustomerView.as_view(), name='customer-list'),
    url(r'^customer/add$', DatabaseCustomerAddView.as_view(), name='customer-add'),
    url(r'^customer/(?P<pk>\d+)$', DatabaseCustomerDetailView.as_view(), name='customer-detail'),
    url(r'^aircraft/$', DatabaseAircraftView.as_view(), name='aircraft-list'),
    url(r'^aircraft/add$', DatabaseAircraftAddView.as_view(), name='aircraft-add'),
    url(r'^aircraft/(?P<pk>\d+)$', DatabaseAircraftDetailView.as_view(), name='aircraft-detail'),
    # url(r'^aircraft/$', DatabaseHomePageView.as_view(), name='aircraft'),
    # url(r'^checks/$', DatabaseHomePageView.as_view(), name='checks'),
    # url(r'^company-data/$', DatabaseHomePageView.as_view(), name='company-data'),
]
