from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from .forms import SignUpForm, TweetForm
from .models import Tweet

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

class MyTweetsView(generic.ListView):
    model = Tweet
    template_name = "twitterclone/tweet_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.select_related('user').filter(user__username__iexact=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tweet_user"] = self.request.user
        return context

class TweetDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tweet
    template_name = 'twitterclone/tweet_confirm_delete.html'
    success_url = reverse_lazy("twitterclone:delete_done")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

class TweetDeleteDoneView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'twitterclone/tweet_delete_done.html'