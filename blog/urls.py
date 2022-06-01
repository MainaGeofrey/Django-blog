from blog import sitemaps
from . import views
from django.urls import path
from .feeds import LatestPostsFeed
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSiteMap

sitemaps = {
    'posts': PostSiteMap
}

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("upload/", views.image_upload_view, name="image_upload"),
    path("weather", views.weatherman, name="weatherman"),
] 
