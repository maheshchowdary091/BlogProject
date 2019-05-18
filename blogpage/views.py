from django.shortcuts import render
from django.http import  HttpResponse
from.models import Post

# Create your views here.

# posts = [
#     {
#         'Writer' : 'Mahesh',
#         'title' : 'My story',
#         'content' : 'This is my first blog',
#         'date_posted' : 'Today'
#     },
#     {
#         'Writer': 'Ashraf',
#         'title': 'Ashraf\'s story',
#         'content': 'This is Ashraf\'s first blog',
#         'date_posted': 'Yesterday'
#     },
# {
#         'Writer': 'Masthan',
#         'title': 'Masthan\'s story',
#         'content': 'This is masthan\'s first blog',
#         'date_posted': 'Apr-30, 2019'
#     }
# ]

def home(request):
    con = {
        'posts': Post.objects.all()
    }
    return render(request, 'blogpage/home.html', con)

def about(request):
    return render(request, 'blogpage/about.html', {'title':'AboutPage'})

