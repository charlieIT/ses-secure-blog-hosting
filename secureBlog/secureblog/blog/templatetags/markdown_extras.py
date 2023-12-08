from django import template
from django.template.defaultfilters import stringfilter
import markdown as md
from blog.models import Category
from blog.views import PostList, PostDetail
# MarkdownX
from django.utils.safestring import mark_safe
from markdownx.utils import markdownify

register = template.Library()

@register.filter()
@stringfilter
def markdown(value):
    return md.markdown(value, extensions=['markdown.extensions.fenced_code'])

@register.simple_tag
def get_categories():
    return Category.objects.all()[0:3]

@register.filter
def formatted_markdown(text):
    return mark_safe(markdownify(text))

"""

    <!--
      {% block navbar %}
      {% include 'navbar.html' %}
    {% endblock navbar %}
    -->
"""