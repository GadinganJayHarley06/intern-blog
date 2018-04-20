from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.views import View, generic


from .models import Post, Index, Category, Tag

class IndexView(View):

    def get(self,request,pk,*args, **kwargs):
        index = Index.objects.get(pk=pk)
        post_list = index.post_set.all()
        paginator = Paginator(post_list, 6)
        page = request.GET.get('page')
        post = paginator.get_page(page)
        
        context = {
                'index':index,
                'post':post,
            }
        return render(request, "index.html", context)


class PostView(View):

    def get(self, request, post_id, *args, **kwargs):
         post = Post.objects.filter(id=post_id).order_by('-date_created')
         context = {'object_list.':post}
         return render(request, "post_list.html", context)