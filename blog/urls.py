from django.urls import path
from .views import (Home,
                    Friend_post,
                    add_like, 
                    add_comment,
                    Post_detail_view,
                    PostUpdateView,
                    Post_DeleteView,
                    delete_comment,
                    Search_query
                    )



urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('friend_post/', Friend_post.as_view(), name='friend_post'),
    path('add_like/', add_like.as_view(), name='add_like'),
    path('add_comment/', add_comment.as_view(), name='add_comment'),
    path('Post_detail_view/<int:pk>', Post_detail_view.as_view(), name='Post_detail_view'),
    path('PostUpdateView/<int:pk>', PostUpdateView.as_view(), name='PostUpdateView'),
    path('Post_DeleteView/<int:pk>', Post_DeleteView.as_view(), name='Post_DeleteView'),
    path('delete_comment', delete_comment.as_view(), name='delete_comment'),
    path('q', Search_query.as_view(), name='search_query'),
]