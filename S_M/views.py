from audioop import reverse
from multiprocessing import context
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from requests import request
from .models import Profile,Comment,Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.auth.decorators import login_required

from . import forms
# Create your views here.
class Comment(LoginRequiredMixin,generic.CreateView):
    model = Comment
    form_class = forms.CommentForm
    success_url = '/'
    template_name = 'S_M/comment_form.html'
    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk = self.kwargs['pk'])
        return context
    def form_valid(self,form):
        form.instance.on_post = Post.objects.get(pk=self.kwargs['pk'])
        form.instance.by_profile = self.request.user.profile
        return super().form_valid(form)
  
'''
@login_required(login_url=reverse_lazy('login'))
def comment(request,pk):
    p=Post.objects.get(pk=pk)
    if request.method == "POST":
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            on_post=p
            by_profile=request.user.profile
            c=Comment(on_post=on_post,by_profile=by_profile,comment=request.POST['comment'])
            c.save()
            return redirect('/')
    form=forms.CommentForm()
    return render(request,'S_M/comment_form.html',{'form':form,'post':p})

'''    

class ListPost(generic.ListView):
    model = Post
    template_name = 'S_M/list_post.html'
    context_object_name = 'posts'
    paginate_by = 10


class CreatePost(LoginRequiredMixin,generic.CreateView):
    model= Post
    form_class = forms.PostForm
    success_url = '/'
    template_name = 'S_M/create_post.html'

    def form_valid(self,form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)
'''
@login_required(login_url=reverse_lazy('login'))
def create_post(request):
    
    if request.method == "POST":
        form = forms.PostForm(request.POST)
        if form.is_valid():
            post= request.POST['post']
            profile= request.user.profile
            p= Post(post=post,profile=profile)
            p.save()
            return redirect('/')
    form = forms.PostForm()
    return render(request,'S_M/create_post.html',{'form':form})

'''
class ListProfiles(generic.ListView):
    model= Profile
    template_name = 'S_M/list_profile.html'
    #queryset = Profile.objects.all()
    paginate_by= 10

class UserProfile(generic.DetailView):
    model = Profile
    template_name = 'S_M/user_profile.html'
    context_object_name = 'user_profile'
    
'''
def list_profiles(request):
    p=Profile.objects.all()
    return render(request,'S_M/list_profile.html',{'profile':p})

def user_profile(request,id):
    up=Profile.objects.get(id=id)
    p=Profile.objects.all()
    return render(request,'S_M/user_profile.html',{'user_profile':up,'profile':p})
'''    
class SignUpView(generic.CreateView):
    form_class=UserCreationForm
    success_url= reverse_lazy('login')
    template_name= "registration/signup.html"

@login_required(login_url=reverse_lazy('login'))
def follow(request,id):
    p=Profile.objects.get(user=request.user.id)
    p.follows.add(id)
    return redirect(reverse_lazy('S_M:profiles'))
    
@login_required(login_url=reverse_lazy('login'))
def un_follow(request,id):
    p=Profile.objects.get(user=request.user.id)
    p.follows.remove(id)
    return redirect(reverse_lazy('S_M:profiles'))
        