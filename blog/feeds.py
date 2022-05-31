from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post
from django.urls import reverse


"""RSS is an abbreviation for Really Simple Syndication, it's a way 
to have information delivered to you instead of you having to go find it.
RSS is basically a structured XML document that includes full or summarized 
text along with other metadata such as published date, author name, etc."""

class LatestPostsFeed(Feed):
    title = "My blog"
    link = ""
    description = "New posts of my blog"
    
    #retrieve object to be included in the feed
    def items(self):
        return Post.objects.filter(status=1)
    
    #receive each item returned by item() and returns title
    def item_title(self, item):
        return item.title
   
       #receive each item returned by item() and returns 
       # description of each item
       #used truncatewords built-in template filter to build the
       # description of the blog post with the first 30 words.
    def item_description(self, item):
        
        return truncatewords(item.content, 30)
    #To retrieve links of items
    # Only needed if the model has no get_absolute_url method
    # def item_link(self, item):
    #     return reverse("post_detail", args=[item.slug])
    
    