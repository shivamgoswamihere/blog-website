from django.shortcuts import render
# Create your views here.
posts=[
    {'author':'Shivam',
     'title':'django',
     'content':'this is my content',
     'date_posted':'July 26,2001'
},
    {'author':'Arshad',
     'title':'MERN',
     'content':'this is is content',
     'date_posted':'April 21,2002'
},
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, "django_app/index.html", context)

def about(request):
    return render(request,"django_app/about.html", {"title": "about"})