from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from django.urls import reverse
from .models import Post
from .forms import PostForm
# Create your views here.

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'home.html'
    def get_success_url(self):
        return reverse('result', kwargs={'pk': self.object.pk})
    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CreatePostView, self).get_form_kwargs(*args, **kwargs)
        return kwargs
class ResultView(DetailView):
    model = Post
    template_name = 'result.html'