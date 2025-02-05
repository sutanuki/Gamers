from django.shortcuts import render
from .models import Thread,Comment,Anchor
from .forms import ThreadForm,CommentForm
from django.views.generic import CreateView
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from django.shortcuts import redirect
import re

def top(request):
    threads = Thread.objects.order_by("-count_comment")[:5]
    return render(request,"top.html",{'threads': threads})
def view(request,id):
    thread = Thread.objects.get(id=id)
    comments = Comment.objects.filter(thread_id=id)
    anchors = Anchor.objects.filter(comment__thread_id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            thread.count_comment+=1
            comment = form.save(commit=False)
            Anchors = [m for m in re.findall(">>"+"\d+",comment.content)]
            comment.content=re.sub(">>\d+","",comment.content)
            comment.thread = thread
            thread.save()
            comment.save()
            if len(Anchors)!=0:
                for i in Anchors:
                    anchor=Anchor(reply_to = int(i[2:]),comment = comment)
                    anchor.save()
            return redirect(reverse('view', args=[thread.id]))
    else:
        form = CommentForm()
    comment_anchors = []
    for comment in comments:
        anchor_for_comment = anchors.filter(comment_id=comment.id).first()
        comment_anchors.append((comment, anchor_for_comment))
    return render(request,"view.html",{'thread': thread,'comments': comments,'comment_anchors': comment_anchors,"form": CommentForm()})
def create(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save()
            return redirect(reverse('view', args=[thread.id]))
    else:
        form = ThreadForm()

    return render(request, 'create.html', {'form': form,})
def index(request):
    threads = Thread.objects.order_by("-created")
    return render(request,"index.html",{'threads': threads})

class ThreadCreate(CreateView):
    model = Thread
    form_class = ThreadForm
    success_url = reverse_lazy('view')

    def get_success_url(self):
        messages.success(self.request, 'スレッドを投稿しました。')
        return reverse_lazy('view',kwargs={'id': self.object.id})
class CommentCreate(CreateView):
    model = Comment
    form_class = CommentForm
    success_url = reverse_lazy('view')

    def get_success_url(self):
        messages.success(self.request, 'コメントを投稿しました。')
        return reverse_lazy('view',kwargs={'id': self.object.id})