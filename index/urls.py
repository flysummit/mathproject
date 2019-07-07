from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^githubtest/',views.github_views),
]
