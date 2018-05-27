from django.conf.urls import url

from .views import WorkOderListView, WorkOderDetailView, TaskDetailView, WorkOderFilteredListView, WorkOderCreateView, TaskCreateView

urlpatterns = [
    url(r'^$', WorkOderListView.as_view(), name='list'),
    url(r'^create/$', WorkOderCreateView.as_view(), name='create'),
    url(r'^(?P<sta>[\w-]+)/$', WorkOderFilteredListView.as_view(), name='filtered'),
    url(r'^detail/(?P<number>[\w-]+)/$', WorkOderDetailView.as_view(), name='detail'),
    url(r'^detail/(?P<number>[\w-]+)/addtask$', TaskCreateView.as_view(), name='add-task'),
    url(r'^detail/(?P<number>[\w-]+)/(?P<pk>\d+)/$', TaskDetailView.as_view(), name='task'),
]
