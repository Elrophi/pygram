from django.shortcuts import redirect, render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from gram.models import Comment, Image
from django.urls import reverse
from django import forms
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View
from django.http import HttpResponseRedirect


# Create your views here.

class ImageList(ListView):
    model = Image

class PostCreate(CreateView):
    model = Image
    fields = ['image', 'description', 'profile']
    success_url = '/'
class CommentForm(forms.Form):
    Comment = forms.CharField()

class PostDetail(DetailView):
    model = Image

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = Comment(
                profile=request.user,
                post=self.get_object(),
                text=comment_form.cleaned_data['Comment']
            )
            comment.save()
        else:
            raise Exception
        return redirect(reverse('detail', args=[self.get_object().id]))

class AddLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Image.objects.get(pk=pk)

        is_dislike = False
        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        is_like = False
        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break
        if is_dislike:
            post.dislikes.remove(request.user)

        if not is_like:
            post.likes.add(request.user)

        if is_like:
            post.likes.remove(request.user)
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

class AddDislike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Image.objects.get(pk=pk)

        is_like = False
        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break
        if is_like:
            post.likes.remove(request.user)

        is_dislike = False
        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            post.dislikes.add(request.user)

        if is_dislike:
            post.dislikes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


