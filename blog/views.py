# -*- coding: utf-8 -*-
from django.views import generic
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from .models import Post, Comment
from .forms import CommentForm, TagSearchForm


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the last five published posts"""
        return Post.objects.order_by('-pub_date')[:5]

    def get_context_data(self, **kwargs):
        form = TagSearchForm()
        context = super(IndexView, self).get_context_data(**kwargs)
        context['form'] = form
        return context


def tag_search(request):
    tag = request.GET.get('tag', None)
    if tag:
        return HttpResponseRedirect(reverse('blog:tag_view', args=(tag,)))
    else:
        return HttpResponseRedirect(reverse('blog:index_view'))


class PostListView(generic.ListView):
    model = Post
    paginate_by = 10
    context_object_name = 'posts'
    template_name = 'blog/posts.html'


class TagView(generic.ListView):
    template_name = 'blog/tags.html'
    context_object_name = 'tagged_post_list'
    paginate_by = 100

    def get_queryset(self):
        # tag_list = self.kwargs['tags'].split('+')
        # tagged_posts = Post.objects.filter(tags__tag_name__in=tag_list)
        tagged_posts = Post.objects.filter(tags__tag_name__iexact=self.kwargs['tag'])
        return tagged_posts

    def get_context_data(self, **kwargs):
        tag = self.kwargs.get('tag', None)
        context = super(TagView, self).get_context_data(**kwargs)
        context['tag'] = tag
        return context


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        form = CommentForm()
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['form'] = form
        return context


class CommentView(generic.FormView):
    template_name = 'blog/post_detail.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('blog:post_view', args=(self.kwargs['post_id'],))

    def form_valid(self, form):
        comment = Comment.objects.create(text=form.cleaned_data['text'], post_id=self.kwargs['post_id'])
        return super(CommentView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        p = get_object_or_404(Post, pk=self.kwargs['post_id'])
        context = super(CommentView, self).get_context_data(**kwargs)
        context['post'] = p
        return context


# def comment(request, post_id):
#     p = get_object_or_404(Post, pk=post_id)
#
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             text = form.cleaned_data['text']
#             comment = Comment.objects.create(text=text, post_id=p.id)
#             return HttpResponseRedirect(reverse('blog:post_view', args=(p.id,)))
#     else:
#         form = CommentForm()
#
#     return render(request, 'blog/post_detail.html', {
#         'form': form,
#         'post': p,
#     })
