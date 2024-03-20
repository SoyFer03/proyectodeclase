from django.shortcuts import render
from .models import Post
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from django.urls import reverse



def index(request):
    post = Post.objects.all()

    return render(request,'index.html', {'post':post})

def post_detail(request,post_id):
    post = Post.objects.get(id=post_id)

    comments = post.comments.filter(active=True)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.post = post 
            new_form.save()
            return HttpResponseRedirect('')

        else:
            pass
           

    return render(request,'post_detail.html', {'post':post, 'comments':comments, 'form':form,})

def enviar_correo(request):
    send_mail(
        'Hola!',
        'Gracias por dejarnos usar tu blog',
        'farteaga010903@gmail.com',
        ['fernandoarteaga507@gmail.com'],
        fail_silently=False,
    )
    return HttpResponseRedirect('/')

