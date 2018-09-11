from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from .models import  Comment
import datetime

def add_comment_to_post(request):
    comment = Comment()
    text = request.POST['text']
    comment.text = text
    ip_address = request.environ['REMOTE_ADDR']
    comment.ip_address = ip_address
    comment.created_date = datetime.datetime.now()
    comment.save()
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)

def all_comments(request):
    comments_list = Comment.objects.all()
    template = loader.get_template('chats/all_comments.html')
    context = { 'comments_list' : comments_list }
    return HttpResponse(template.render(context, request))
