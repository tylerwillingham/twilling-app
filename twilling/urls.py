from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views

urlpatterns = [
    url(r'^blog/posts/$', views.PostList.as_view()),
    url(r'^blog/statuses/$', views.StatusList.as_view()),
    url(r'^blog/categories/$', views.CategoryList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)