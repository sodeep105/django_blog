from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts =[
    { 'author' : 'Sudip Sengupta',
    'title' : 'Django tutorials',
    'content' : 'Programming',
    'date_posted' : '10th May, 2020'
},
{
    'author':'Pritha Das',
    'title' : 'Mandala',
    'content' : 'Art',
    'date_posted' : '10th May 2020'
}


]

# Create your views here.
def Home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request,'blog/home.html', context)

def About(request):
    return render(request,'blog/about.html')
