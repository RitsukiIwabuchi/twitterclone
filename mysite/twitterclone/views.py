from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import SignUpForm, TweetForm
from .models import Tweet, Follow

class IndexView(generic.TemplateView):
    template_name = 'twitterclone/index.html'

class LogoutDoneView(generic.TemplateView):
    template_name = 'twitterclone/logout_done.html'

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = "twitterclone/signup.html" 
    success_url = reverse_lazy('twitterclone:index')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        return HttpResponseRedirect(self.get_success_url())

class CreateTweetView(LoginRequiredMixin, generic.CreateView):
    form_class = TweetForm
    template_name = "twitterclone/tweet_create.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class MyTweetsView(LoginRequiredMixin, generic.ListView):
    model = Tweet
    template_name = "twitterclone/tweet_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.select_related('user').filter(user__username__iexact=self.kwargs.get("username"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tweet_user"] = self.kwargs.get("username")
        return context

class HomeTweetView(LoginRequiredMixin, generic.ListView):
    model = Tweet
    template_name = "twitterclone/tweet_list_home.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__in=Follow.objects.filter(follow_user=self.request.user).values('followed_user'))

class TweetDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tweet
    template_name = 'twitterclone/tweet_confirm_delete.html'
    success_url = reverse_lazy("twitterclone:delete_done")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

class TweetDeleteDoneView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'twitterclone/tweet_delete_done.html'

class UserListView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = 'twitterclone/user_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.exclude(username__iexact=self.request.user.username)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["followers"] = Follow.objects.filter(follow_user=self.request.user).values_list('followed_user_id', flat=True)
        return context

class FollowView(LoginRequiredMixin, generic.TemplateView):
    def post(self, request, **kwargs):
        user_pk = request.POST.get('user_pk')
        follower = get_object_or_404(User, pk=user_pk)
        follow = Follow(follow_user=self.request.user, followed_user=follower)
        follow.save()
        return redirect(reverse("twitterclone:userlist"))

class FollowDeleteView(LoginRequiredMixin, generic.TemplateView):
    def post(self, request, **kwargs):
        user_pk = request.POST.get('user_pk')
        follower = get_object_or_404(User, pk=user_pk)
        follow = get_object_or_404(Follow, follow_user=self.request.user, followed_user=follower)
        follow.delete()
        return redirect(reverse("twitterclone:userlist"))

class FavoriteView(LoginRequiredMixin, generic.TemplateView):
    def post(self, request, **kwargs):
        tweet_pk = request.POST.get('tweet_pk')
        tweet = get_object_or_404(Tweet, pk=tweet_pk)
        tweet.favorites.add(request.user)
        tweet.save()
        return redirect(reverse("twitterclone:home-tweets"))

class FavoriteDeleteView(LoginRequiredMixin, generic.TemplateView):
    def post(self, request, **kwargs):
        tweet_pk = request.POST.get('tweet_pk')
        tweet = get_object_or_404(Tweet, pk=tweet_pk)
        tweet.favorites.remove(request.user)
        tweet.save()
        return redirect(reverse("twitterclone:home-tweets"))