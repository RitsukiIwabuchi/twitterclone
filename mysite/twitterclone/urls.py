from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'twitterclone'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='twitterclone/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/done/', views.LogoutDoneView.as_view(), name = 'logout_done'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('new/', views.CreateTweetView.as_view(), name='new'),
    path('my-tweets/<username>', views.MyTweetsView.as_view(), name='my-tweets'),
    path('home-tweets/', views.HomeTweetView.as_view(), name='home-tweets'),
    path('delete/<int:pk>', views.TweetDeleteView.as_view(), name='delete'),
    path('delete/done/', views.TweetDeleteDoneView.as_view(), name='delete_done'),
    path('userlist/', views.UserListView.as_view(), name='userlist'),
    path('follow/', views.FollowView.as_view(), name='follow'),
    path('follow/delete/', views.FollowDeleteView.as_view(), name='followdelete'),
    path('favorite/<int:pk>', views.FavoriteView.as_view(), name='favorite'),
    path('favorite/<int:pk>/delete/', views.FavoriteDeleteView.as_view(), name='favoritedelete'),
]
