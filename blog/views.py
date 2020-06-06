from django.shortcuts import render

posts =[
    {
        'title':'Data Science',
        'author':'Ebin Baby',
        'Date':'June 2020',
        'Content':'Data science is cool!!',
    },
    {
        'title':'Machine Learning',
        'author':'Ebin Baby',
        'Date':'June 2020',
        'Content':'Machine Learning is Amazing!!',
    },
    {
        'title':'Python',
        'author':'Ebin Baby',
        'Date':'June 2020',
        'Content':'Python is incredible!!',
    }
]

def home(request):
    context={
        'posts':posts
    }
    return render(request,'blog/home.html',context)
def about(request):
    return render(request,'blog/about.html',{'title':'About'})

