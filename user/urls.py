from django.urls import path
from .views import (Profile, 
                    Users_list,
                    send_friend_request, 
                    accept_friend_request, 
                    delete_friend_request, 
                    cancel_friend_request,
                    Unfriend,
                    Friend_profile,
                    Register_user
                    )



urlpatterns = [
    path('profile/',Profile.as_view(), name='profile'),
    path('all_users/', Users_list.as_view(), name='all_users'),
    path('send_friend_request/<int:id>', send_friend_request.as_view(), name='send_friend_request'),
    path('accept_friend_request/<int:id>', accept_friend_request.as_view(), name='accept_friend_request'),
    path('delete_friend_request/<int:id>', delete_friend_request.as_view(), name='delete_friend_request'),
    path('cancel_friend_request/<int:id>', cancel_friend_request.as_view(), name='cancel_friend_request'),
    path('unfriend/<int:id>', Unfriend.as_view(), name='unfriend'),
    path('friend_profile/<int:id>', Friend_profile.as_view(), name='friend_profile'),
    path('register', Register_user.as_view(), name='register'),
]