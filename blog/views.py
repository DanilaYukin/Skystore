from .models import Blog
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'content', 'preview']
    template_name = 'blog/blog_form.html'
    context_object_name = 'blog'
    success_url = reverse_lazy('myblog:blogs_list')


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blogs_list.html'
    context_object_name = 'blogs'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'


class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'blog/blog_form.html'
    fields = ['content', 'publication_sign', 'title', 'preview']
    success_url = reverse_lazy('myblog:blogs_list')


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('myblog:blogs_list')
