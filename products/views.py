from django.views.generic import ListView, DetailView

from .models import Post, Category

class HomeView(ListView):
    model = Post
    template_name = "blog/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get("slug")).select_related('category')

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    slug_url_kwarg = 'post_slug'

