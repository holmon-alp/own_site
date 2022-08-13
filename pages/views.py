from django.urls import reverse_lazy
from django.shortcuts import render
from django.template import loader
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from . import models
from django.utils import timezone
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_deny
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.shortcuts import render, get_object_or_404
from .forms import CommentForm
from django.contrib import messages

class HomeView(ListView):
	model = models.BlogPost
	template_name = 'home.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context


class BlogView(CreateView):
	model = models.BlogPost
	fields = ['title', 'about', 'image']
	# form_class = forms.PostForm
	template_name = 'create_view.html'
	success_url = reverse_lazy('home')

class BlogDelete(DeleteView):
   model = models.BlogPost
   template_name='delete_view.html'
   success_url = reverse_lazy("home")


class CertifView(ListView):
	model = models.Certificat
	template_name = 'certificate.html'
	context_object_name = 'cers'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context

	@xframe_options_deny
	def view_one(request):
	    return HttpResponse("I won't display in any frame!")

	@xframe_options_sameorigin
	def view_two(request):
	    return HttpResponse("Display in a frame if it's from the same origin as me.")

# class BlogDetail(DetailView):
# 	model = models.BlogPost
# 	template_name = 'blog-detail.html'
# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		return context

def is_no_repeat(pk, request):
	post = get_object_or_404(models.BlogPost, pk=pk)
	comments = post.comments.filter(body=request.POST['body'])
	if comments:
		return False
	else:
		return True

def blog_detail(request, pk):
    template_name = 'blog-detail.html'
    post = get_object_or_404(models.BlogPost, pk=pk)
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid() and is_no_repeat(pk, request):
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()

    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})