
from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=159, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    #metadata, sorting
    class Meta:
        ordering = ['-created_on']
    
    #default human-readable representation of the object. 
    def __str__(self):
        return self.title
    

    #To retrieve links of items for SEO reference, generate feeds e.t.c
    #tell Django how to calculate the canonical URL(official url for a page)
    # for an object
    def get_absolute_url(self):
        from django.urls import reverse
        
        #generate unique url for each post/product,,add sitemap info to each post
        return reverse("post_detail", kwargs={"slug": str(self.slug)})
   
        
        

class Comment(models.Model):
    """Foreign key relation that establishes a many-to-one relationship with the Post model, 
    since every comment will be made on a post and each post will have multiple comments.
    related name allows us to, retrieve the post of a comment object using comment.post """
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    #admin approves comments to avoid spam
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
    

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image')
    #upload_to uploads images to  MEDIA_ROOT/images/ by default
    #custom load_to: image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    def __str__(self):
        return self.title
    

#News aggregator
#save data scraped website to database
class Headline(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(null=True, blank=True)
    url = models.URLField(blank=True)
    
    def __str__(self):
        return self.title
    
    
