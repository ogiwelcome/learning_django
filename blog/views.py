from django.shortcuts import render

from django.views.generic import ListView

from .models import BlogPost

class IndexView(ListView):
    """トップページのビュー
    Attributes:
        template_name: レンダリングするテンプレート
    """
    template_name = 'index.html'
    context_object_name = 'orderby_records'
    queryset = BlogPost.objects.order_by('-posted_at')