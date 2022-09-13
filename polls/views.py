from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse

from django.views import View

import article
from .forms import PollForm
from django.contrib import messages



# Create your views here.
class FeedBackView(View):
    def get(self,request,id):
        form = PollForm(None)
        #poll = get_object_or_404(Poll,id=id)
        context = {'form': form}
        return render(request, 'feedback.html', context)
    def post(self,request,id):
        form = PollForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            poll = form.save(commit=False)


            poll.article_name_id = id
            poll.save()

            messages.success(request, "Evaluation has been successfully created")
            return redirect("index")

        #poll = get_object_or_404(Poll)
        context = {'form': form}
        return render(request, 'feedback.html', context)




class SuccessView(View):
    def get(self,request):
        return render(request, 'success.html')

