from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

import article
from .forms import ArticleForm #,PollForm
from django.contrib import messages
from .models import Article,Comment #,Poll
# Create your views here.

class ArticlesView(View):
    def get(self,request,*args,**kwargs):
        keyword = request.GET.get("keyword")

        if keyword:
            articles = Article.objects.filter(title__contains=keyword)
            return render(request, "articles.html", {"articles": articles})

        articles = Article.objects.all()

        return render(request, "articles.html", {"articles": articles})



#---------------------------------
class IndexView(View):
    def get(self,request):
        return render(request,"index.html")

#---------------------------------------------

class AboutView(View):
    def get(self,request):
        return render(request, "about.html")



#-----------------------------------------------------------
class DashboardView(View):
    @method_decorator(login_required(login_url="user:login"))
    def get(self,request):
        articles = Article.objects.filter(author=request.user)
        context = {
            "articles": articles
        }

        return render(request, "dashboard.html", context)



#----------------------------------------------------------
class DetailView(View):
    @method_decorator(login_required(login_url="user:login"))
    def get(self,request,id):
        article = get_object_or_404(Article, id=id)
        comments = article.comments.all()
        return render(request, "detail.html", {"article": article, "comments": comments})



#-------------------------------------------------
#fix it as a form method
class AddArticleView(View):
    @method_decorator(login_required(login_url="user:login"))
    def get(self,request):
        form = ArticleForm( None)

        return render(request, "addarticle.html", {"form": form})

    @method_decorator(login_required(login_url="user:login"))
    def post(self, request):
        form = ArticleForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            article = form.save(commit=False)

            article.author = request.user
            article.save()

            messages.success(request, "Course has been successfully created")
            return redirect("index")

        return render(request, "addarticle.html", {"form": form})


#--------------------------------

class UpdateArticleView(View):
    @method_decorator(login_required(login_url="user:login"))
    def get(self,request,id):
        article = get_object_or_404(Article, id=id)

        form = ArticleForm(None, instance=article)
        return render(request, "update.html", {"form": form})

    @method_decorator(login_required(login_url="user:login"))
    def post(self, request, id):
        article = get_object_or_404(Article, id=id)

        form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
        if form.is_valid():
            article = form.save(commit=False)

            article.author = request.user
            article.save()

            messages.success(request, "Article has been succesfully updated")
            return redirect("article:dashboard")

        return render(request, "update.html", {"form": form})


#---------------------------------------------

class DeleteArticleView(View):
    @method_decorator(login_required(login_url="user:login"))
    def get(self,request,id):
        article = get_object_or_404(Article, id=id)
        article.delete()
        messages.success(request, "Course has been deleted succesfully")
        return redirect("article:dashboard")



#----------------------------------------------------------------

class AddCommentView(View):
    def post(self,request,id,*args,**kwargs):
        article = get_object_or_404(Article, id=id)
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author=comment_author, comment_content=comment_content)
        newComment.article = article

        newComment.save()
        return redirect(reverse("article:detail", kwargs={"id": id}))

"""class FeedBackView(View):
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

"""