from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

import article
from .forms import ArticleForm
from django.contrib import messages
from .models import Article,Comment
from user.decorators import teacher_required,student_required

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


class AddArticleView(View):

    @method_decorator(login_required(login_url="user:login"))
    @method_decorator(teacher_required(login_url="user:loginins"))
    def get(self,request):
        form = ArticleForm( None)

        return render(request, "addarticle.html", {"form": form})


    #@method_decorator(login_required(login_url="user:login"))
    @method_decorator(login_required(login_url="user:login"))
    @method_decorator(teacher_required(login_url="user:loginins"))
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

## add teacher required methods to necessary articleviews
class UpdateArticleView(View):
    @method_decorator(login_required(login_url="user:login"))
    @method_decorator(teacher_required(login_url="user:loginins"))
    def get(self,request,id):
        article = get_object_or_404(Article, id=id)

        form = ArticleForm(None, instance=article)
        return render(request, "update.html", {"form": form})

    @method_decorator(login_required(login_url="user:login"))
    @method_decorator(teacher_required(login_url="user:loginins"))
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
    @method_decorator(teacher_required(login_url="user:loginins"))
    def get(self,request,id):
        article = get_object_or_404(Article, id=id)
        article.delete()
        messages.success(request, "Course has been deleted succesfully")
        return redirect("article:dashboard")



#----------------------------------------------------------------

class AddCommentView(View):
    @method_decorator(login_required(login_url="user:login"))
    @method_decorator(student_required(login_url="user:loginstu"))
    def post(self,request,id,*args,**kwargs):
        article = get_object_or_404(Article, id=id)
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author=comment_author, comment_content=comment_content)
        newComment.article = article

        newComment.save()
        return redirect(reverse("article:detail", kwargs={"id": id}))

