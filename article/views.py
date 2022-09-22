from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.db.models import Avg,Q


import article
from .forms import ArticleForm,VideoForm
from django.contrib import messages
from .models import Article,Comment,TakenCourse,Video

from user.decorators import teacher_required,student_required
from user.models import Student,User

# Create your views here.

class ArticlesView(View):
    def get(self,request,*args,**kwargs):
        keyword = request.GET.get("keyword")

        #articles = []
        articles = Article.objects.annotate(avg_score=Avg('taken_courses__score'))
        if request.user.is_student:
            student = get_object_or_404(Student, user_id=request.user.id)
            # a loop to check the courses that are not taken by this student and these courses will be added to articles list
            for course in Article.objects.all():
                if course in student.courses.all():
                    articles = articles.exclude(title__contains=course.title)
                else:
                    pass  #articles.append(course)

            #later find a way to filter available courses for student
            if keyword:
                articles = articles.filter(title__icontains=keyword)
                return render(request, "articles.html", {"articles": articles})



            return render(request, "articles.html", {"articles": articles})


        if keyword:
            articles = articles.filter(title__icontains=keyword)
            return render(request, "articles.html", {"articles": articles})


        #articles = Article.objects.all()


        return render(request, "articles.html", {"articles": articles})

#----------------------------------------------

class TakenCoursesView(View):
    def get(self, request, *args, **kwargs):
        keyword = request.GET.get("keyword")
        student = get_object_or_404(Student, user_id=request.user.id)
        courses = student.courses.annotate(avg_score=Avg('taken_courses__score'))


        if keyword:
            courses = courses.filter(title__icontains=keyword)
            return render(request, "taken-courses.html", {"courses": courses})


        return render(request, "taken-courses.html", {"courses": courses})






#----------------------------------------------
class IndexView(View):
    def get(self,request):
        """if request.user.is_teacher:
            articles = Article.objects.filter(author=request.user)
            context = {
                "articles": articles
            }
            return render(request,"dashboard.html",context)
"""
        articles = Article.objects.annotate(avg_score=Avg('taken_courses__score')).order_by('-avg_score')


        return render(request,"index.html",{"articles":articles})

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

class VideosView(View):
    @method_decorator(login_required(login_url="user:login"))
    def get(self,request,id):
        article = get_object_or_404(Article, id=id)
        videos = article.videos.all()
        return render(request, "videos.html", {"videos": videos})


#-------------------------------------------------
class AddVideosView(View):
    @method_decorator(login_required(login_url="user:login"))

    def get(self, request,id):
        form = VideoForm(None)

        return render(request, "videopage.html", {"form": form})


    @method_decorator(login_required(login_url="user:login"))

    def post(self, request,id):
        form = VideoForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            video = form.save(commit=False)
            article = get_object_or_404(Article, id=id)
            video.title = request.POST.get('title')
            video.url = request.POST.get('url')
            video.article = article
            video.save()

            messages.success(request, "Course has been successfully created")
            return redirect("article:dashboard")

        return render(request, "videopage.html", {"form": form})

#----------------------------------------------


#-------------------------------------------------


class AddArticleView(View):

    @method_decorator(login_required(login_url="user:login"))
    @method_decorator(teacher_required(login_url="user:loginins"))
    def get(self,request):
        form = ArticleForm(None)

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
            return redirect("article:dashboard")

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
        messages.success(request, "Course has been deleted successfully")
        return redirect("article:dashboard")



#----------------------------------------------------------------

class AddCommentView(View):
    @method_decorator(login_required(login_url="user:login"))
    @method_decorator(student_required(login_url="user:loginstu"))
    def post(self,request,id,*args,**kwargs):
        article = get_object_or_404(Article, id=id)
        student = get_object_or_404(Student, user_id=request.user.id)
        if article in student.courses.all():
            comment_content = request.POST.get("comment_content")

            newComment = Comment(comment_author=request.user.username, comment_content=comment_content)
            newComment.article = article

            newComment.save()
            return redirect(reverse("article:detail", kwargs={"id": id}))


        messages.warning(request, "You cannot comment on a course that you don't take")
        return redirect("article:takencourses")

class TakeCourse(View):
    @method_decorator(login_required(login_url="user:login"))
    @method_decorator(student_required(login_url="user:loginstu"))
    def get(self,request,id,*args,**kwargs):
        article = get_object_or_404(Article,id=id)
        student = get_object_or_404(Student,user_id=request.user.id)
        if article in student.courses.all():
            messages.warning(request, "You cannot take a course more than once")
            return redirect("article:takencourses")


        taken_course = TakenCourse()
        taken_course.student = student

        taken_course.article = article
        taken_course.score = 0
        taken_course.save()
        messages.warning(request, "Take course action completed succesfully!!")
        return redirect("article:takencourses")


class DropCourse(View):
    @method_decorator(login_required(login_url="user:login"))
    @method_decorator(student_required(login_url="user:loginstu"))
    def get(self,request,id,*args,**kwargs):
        article = get_object_or_404(Article, id=id)
        student = get_object_or_404(Student, user_id=request.user.id)
        if article in student.courses.all():
            takencourse = get_object_or_404(TakenCourse,article_id =id,student_id=request.user.id)
            takencourse.delete()
            messages.success(request, "Course has been dropped succesfully")
            return redirect("article:takencourses")


        messages.warning(request, "You cannot drop a couser that you don't own")
        return redirect("article:takencourses")


class RateCourse(View):
    @method_decorator(login_required(login_url="user:login"))
    @method_decorator(student_required(login_url="user:loginstu"))
    def post(self,request,*args,**kwargs):
        #print(request.POST)
        id=request.POST['article_id']
        article = get_object_or_404(Article, id=id)
        student = get_object_or_404(Student, user_id=request.user.id)
        if article in student.courses.all():
            takencourse = get_object_or_404(TakenCourse,article_id =id,student_id =request.user.id)
            takencourse.score = request.POST.get('val') # it should be the score that student gave
            takencourse.save()
            messages.success(request, "Course has been rated successfully")
            return redirect(reverse("article:detail", kwargs={"id": id}))



        return redirect("article:detail")