from django.contrib.sitemaps import Sitemap
from .models import Post

#generate SEO XML/ sitemap
#sitemap configuration
class PostSiteMap(Sitemap):
    #always, hourly, daily, monthly, yearly never
    changerfreq = "weekly"
    #relevance of post pages, max=1
    priority = 0.8 
    
    def items(self):
        return Post.objects.filter(status=1)
    
    def lastmod(self, obj):
        return obj.updated_on
    
    #add location()
    #either implement location() on your PostSitemap, or implement
    #get_absolute_url() on your Post model.