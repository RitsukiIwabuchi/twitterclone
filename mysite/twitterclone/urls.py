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
    path('new/', views.CreateTweet.as_view(), name='new'),
    path('my-tweets/<username>', views.MyTweets.as_view(), name='my-tweets'),
    path('delete/<int:pk>', views.TweetDelete.as_view(), name='delete'),
    path('delete/done/', views.DeleteDone.as_view(), name='delete_done'),
]
