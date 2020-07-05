from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import View
from .models import Profile, FriendRequest
from blog.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from .form import UserUpdateForm, UserProfileUpdateForm, UserRegisterForm
from django.contrib.auth import authenticate, login


class Profile(LoginRequiredMixin,View):
    def get(self, request,):
        user = request.user
        request_i_send = FriendRequest.objects.filter(from_user=user)
        request_i_get = FriendRequest.objects.filter(to_user=user)
        u_form = UserUpdateForm(instance=self.request.user)
        p_form = UserProfileUpdateForm(instance=self.request.user.profile)
        my_post = Post.objects.filter(user=user.profile).order_by('-id')
        context ={
            'request_i_send': request_i_send,
            'request_i_get': request_i_get,
            'u_form': u_form,
            'p_form': p_form,
            'posts': my_post,
        }
        return render(request,'user/profile.html',context)
    def post(self, request):
        u_form = UserUpdateForm(request.POST,instance=self.request.user)
        p_form = UserProfileUpdateForm(request.POST, request.FILES, instance=self.request.user.profile)
        if u_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')


class Users_list(LoginRequiredMixin,View):
    def get(self,request):
        user= request.user.id
        users_list = User.objects.exclude(profile__friend=user)
        
        context = {
            'friends': users_list,
        }
        return render(request, 'user/Friend.html',context)

class send_friend_request(LoginRequiredMixin,View):
    def get(self,request,id):
        to_user = User.objects.get(id=id)
        from_user = request.user
        frequest, created = FriendRequest.objects.get_or_create(from_user=from_user,to_user=to_user)
        return redirect('all_users')

class accept_friend_request(LoginRequiredMixin,View):
    def get(self,request,id):
        user1 = request.user
        user2 = User.objects.get(id=id)
        frequest = FriendRequest.objects.get(from_user=user2, to_user=user1)
        user1.profile.friend.add(user2.profile)
        user2.profile.friend.add(user1.profile)
        frequest.delete()
        return redirect('profile')

class delete_friend_request(LoginRequiredMixin,View):
    def get(self,request,id):
        user1 = request.user
        user2 = User.objects.get(id=id)
        frequest = FriendRequest.objects.get(from_user=user2, to_user=user1)
        frequest.delete()
        return redirect('profile')

class cancel_friend_request(LoginRequiredMixin,View):
    def get(self,request,id):
        user1 = request.user
        user2 = User.objects.get(id=id)
        frequest = FriendRequest.objects.get(from_user=user1, to_user=user2)
        frequest.delete()
        return redirect('profile')

class Unfriend(LoginRequiredMixin, View):
    def get(self, request, id):
        user1 = request.user
        user2 = User.objects.get(id=id)
        user1.profile.friend.remove(user2.profile)
        user2.profile.friend.remove(user1.profile)
        return redirect('profile')

class Friend_profile(LoginRequiredMixin, View):
    def get(self,request,id):
        friend = User.objects.get(id=id)
        posts = Post.objects.filter(user=friend.profile).order_by('-id')
        context = {
            'friend': friend,
            'posts': posts,
        }
        return render(request, 'user/friend_profile.html', context)

class Register_user(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'user/register.html', {'form':form})
    def post(self,request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect ('home')
        return redirect ('register')