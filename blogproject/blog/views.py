from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog
from django.utils import timezone
# Create your views here.
def home(request):
    blogs = Blog.objects # 쿼리셋을 들고옴.
    return render(request, 'home.html',{'blogs' : blogs}) # Blog의 모든 객체들이 쿼리셋으로 template에 보내짐.


def detail(request,blog_id):
    detail = get_object_or_404(Blog, pk= blog_id)
    return render(request, 'detail.html', { 'detail':detail })

def new(request):
    return render(request,'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()

    blog.save() #객체저장

    return redirect('/blog/'+str(blog.id)) # => '/blog/blog.id(숫자)'