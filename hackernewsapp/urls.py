from django.contrib import admin
from django.urls import path,include
from .views import *
from django.views.generic import TemplateView


urlpatterns = [
    path('',PostListView, name='home'),
    path('new',NewPostListView, name='new_home'),
    path('past',PastPostListView, name='past_home'),
    path('user/<username>', UserInfoView, name='user_info'),
    path('posts/<username>',UserSubmissions, name='user_post'),
    path('post/<int:id>',CommentListView, name='post'),
    path('submit',SubmitPostView, name='submit'),
    path('signin',signin, name='signin'),
    path('signup',signup, name='signup'),
    path('signout',signout, name='signout'),
    path('vote/<int:id>',UpVoteView,name='vote'),
    path('downvote/<int:id>',DownVoteView,name='dvote'),
    path('post/<int:id1>/comment/<int:id2>',CommentReplyView,name='reply'),
    path('edit/<int:id>',EditListView, name='edit'),
    path('',TemplateView.as_view(template_name="social_app/index.html")),
]

