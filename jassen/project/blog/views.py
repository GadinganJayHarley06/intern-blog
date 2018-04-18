from django.shortcuts import render
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import get_user_model
from django.views.generic import (ListView,DetailView,CreateView,UpdateView)
from .models import Post,Category,Tags,Index 
from django.views import generic, View
# Create your views here.

class IndexView(View):
    def get(self, request, pk, *args, **kwargs):
        index = Index.objects.filter(pk=pk)
        context = {'index':index,}
        return render(request, "index.html", context)


class PostView(View):
    def get(self, request, post_id, *args, **kwargs):
        post_list = Post.objects.all()
        paginator = Paginator(post_list, 1)
        page = request.GET.get('page')
        post = paginator.get_page(page)
        context = {'post':post,}
        return render(request, "Post_list.html", context)
 