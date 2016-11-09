from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from project.models import login

urlpatterns = patterns('',

    url(r'^',ListView.as_view(
    						queryset=login.objects.all().order_by("-created")[:2],
    						template_name="blog.html")),
)
