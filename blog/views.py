from django.shortcuts import render, redirect
from django.views.generic import View, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Like, Comment
from django.contrib.auth.models import User
from .form import add_post
from user.models import Profile
from django.db.models import Q



class Home(LoginRequiredMixin, View):
    def get(self,request):
        posts = Post.objects.all().order_by('-id')        
        form = add_post()
        context = {
            'posts': posts,
            'form': form,
        }
        return render(request, 'blog/Home.html', context)
    def post(self,request):
        data = add_post(request.POST, request.FILES)
        next_ = request.POST['next']
        if data.is_valid():
            data.instance.user = self.request.user.profile
            data.save()
            return redirect(next_)

class Post_detail_view(LoginRequiredMixin, View):
    def get(self,request,pk):
        post = Post.objects.get(id=pk)
        user= self.request.user.profile
        see = 'Null'
        if post.user == user:
            see = True
        else:
            see = False
        context = {
            'post': post,
            'see': see
        }
        return render(request, 'blog/post_detail.html',context)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title','content','image']
    template_name = 'blog/post_update.html'
    success_url = '/'
    def form_valid(self, form):
        form.instance.user = self.request.user.profile
        return super().form_valid(form)

class Post_DeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_update.html'
    success_url = '/'

class Friend_post(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        posts = Post.objects.filter(user__friend__user=user).order_by('-id')
        context = {
            'posts': posts,
        }
        return render(request, 'blog/friend_post.html', context)

class add_like(LoginRequiredMixin, View):
    def post(self,request):
        post_id = request.POST['post_id']
        post = Post.objects.get(id=post_id)
        next_ = request.POST['next']
        user = request.user.profile
        # llll = Like.objects.filter(user=user).delete()
        like, created = Like.objects.get_or_create(post=post, user=user)
        if not created:
            if like.value=='unlike':
                like.value='like'
            elif like.value=='like':
                like.value='unlike'
        else:
            like.value='like'
        like.save()
        return redirect(next_)

class add_comment(LoginRequiredMixin, View):
    def post(self,request):
        post_id = int(request.POST['post_id'])
        next_ = request.POST['next']
        post = Post.objects.get(id=post_id)
        user = request.user.profile
        value = request.POST['comment']
        Comment.objects.create(post=post,user=user,value=value)
        return redirect(next_)


class delete_comment(LoginRequiredMixin,View):
    def post(self, request):
        next_ = request.POST['next']
        comment_id=request.POST['comment_id']
        comment = Comment.objects.get(id=comment_id).delete()
        return redirect(next_)


class Search_query(LoginRequiredMixin, View):
    def get(self,request):
        query = request.GET.get("q", None)
        blog = Post.objects.all().order_by('-id')
        if query is not None:
            blog = blog.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
                ).order_by('-id')
        context = {
            "posts": blog,
            'query': query
        }
        return render(request, 'blog/query_in_post.html', context)
