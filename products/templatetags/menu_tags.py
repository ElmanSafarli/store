from django import template
from products.models import Category, Post

register = template.Library()

# @register.simple_tag()
# def get_list_category():
#     """Вывод всех категорий"""
#     return get_all_categories()


@register.inclusion_tag('blog/include/tags/top_menu.html')
def get_categories():
    category = Category.objects.all() #.order_by("name")
    return {"list_category": category}

@register.inclusion_tag('blog/include/tags/last_post_tag.html')
def get_last_posts():
    posts = Post.objects.select_related("category").order_by("id")[:5]
    return {"list_last_posts": posts}