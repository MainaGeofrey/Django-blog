from re import template
from django.views import generic
from .models import Headline, Post 
from .forms import CommentForm, ImageForm
from django.shortcuts import redirect, render, get_object_or_404
from bs4 import BeautifulSoup as Bsoup
import requests

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    
    #Pagination
    #ListView has inbuilt support for pagination
    #GET parameter controls pagination
    #paginate by 3 posts a page
    paginate_by = 3


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
    
#validate and save
def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})

from django.shortcuts import render
# import json to load json data to python dictionary
import json
# urllib.request to make a request to api
import urllib.request








def weatherman(request):
    if request.method == 'POST':
        city = request.POST['city']
        
        # source contain JSON data from API
        start_url = 'http://api.openweathermap.org/data/2.5/weather?q ='+ city + '&appid = c2204035ae362425fe80f157c60a03f0'
        url = start_url.replace(' ', '')
        
        source =  urllib.request.urlopen(url).read()
        
        # converting JSON data to a dictionary
        list_of_data = json.loads(source)
        
        data = {
            "country_code": str(list_of_data['sys']['country']),
			"coordinate": str(list_of_data['coord']['lon']) + ' '
						+ str(list_of_data['coord']['lat']),
			"temp": str(list_of_data['main']['temp']) + 'k',
			"pressure": str(list_of_data['main']['pressure']),
			"humidity": str(list_of_data['main']['humidity']),
        }
        
        print(data)
        
    else:
        data = {}
    return render(request, "weatherman.html", data)


#News aggregator
#save data scraped website to database

def scrape(request):
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = "https://www.theonion.com/"
    
    content = session.get(url, verify=False).content
    soup = Bsoup(content, "html.parser")
    News = soup.find_all('div', {"class":"curation-module__item"})
    for article in News:
        main = article.find_all('a')[0]
        link = min['href']
        image_src = str(main.find('img')['srcset']).split(" ")[-4] 
        title = main['title']
        new_headLine = Headline()
        new_headLine.title = title
        new_headLine.url = link
        new_headLine.image = image_src
        new_headLine.save()
        return redirect("news.html")
    
    
#Serve the stored database objects
def news_list(request):
    headlines = Headline.objects.all()[::1]
    context = {
        'object_list': headlines,
    }
    return render(request, "news.html", context)