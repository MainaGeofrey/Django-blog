from re import template
from django.views import generic
from .models import Post
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    #approved comments
    comments = post.comments.filter(active=True)
    
    #initialized to none since it is the page where user will create post
    new_comment = None
    
    # Comment posted
    if request.method == 'POST':
        #user input
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            
            #Create Comment object but don't save to db
            #commit=False which will prevent it from saving into the database 
            # right away because we still have to link it the post object
            new_comment = comment_form.save(commit=False)
            #Assign current post to comment
            new_comment.post = post
            #save the comment to db
            new_comment.save()
    else:
        comment_form = CommentForm()
        
    return render(request,template_name, {'post': post,
                                'comments':comments,
                                'new_comment': new_comment,
                                'comment_form': comment_form  
                                        })