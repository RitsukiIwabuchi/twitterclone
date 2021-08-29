from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from .forms import SignUpForm

class IndexView(generic.TemplateView):
    template_name = 'twitterclone/index.html'

class SignUpView(generic.edit.CreateView):
    form_class = SignUpForm
    template_name = "twitterclone/signup.html" 
    success_url = reverse_lazy('twitterclone:index')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        return HttpResponseRedirect(self.get_success_url())