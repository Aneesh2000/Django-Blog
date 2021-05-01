from django.shortcuts import render,redirect
from .forms import BlogForm

# Create your views here.
def blog_list(request):
    return render(request,"blog_register/blog_list.html")

def blog_form(request):
    if request.method =="GET":
        form = BlogForm()
        return render(request,"blog_register/blog_form.html",{'form':form})
    else:
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect()

def blog_delete(request):
    return