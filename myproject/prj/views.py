from django.shortcuts import render , get_object_or_404
from .models import Article , Category
from django.core.paginator import Paginator
from django.views.generic import ListView , DetailView
from account.models import User
from account.mixins import AuthorAccessMixin

#https://docs.djangoproject.com/en/4.1/topics/http/views/
#https://docs.djangoproject.com/en/4.1/topics/http/shortcuts/

# My home page *shortcuts*.
  
# def home(request , page=1):
#     article_list = Article.objects.status()
#     paginator = Paginator(article_list , 3)
#     # page = request.GET.get('p')
#     article = paginator.get_page(page)
#     return render(request , "prj/home.html" ,{
#        'contexts' : article ,
#     })

# My home page *generic*.
class ArticleListview(ListView):
    paginate_by = 3
    queryset = Article.objects.status()

    
    # model = Article
    # template_name = "prj/home.html"
    # context_object_name = "contexts"
    
    
# My home page information *shortcuts*.
# def detail(request , slug):
#     return render(request , "prj/detail.html" , {
#         'article' : get_object_or_404(Article.objects.status() , slug=slug )
#     })
    
# My home page information *generic*.    
class ArticleDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        article =  get_object_or_404(Article.objects.status() , slug=slug )
        
        ip_ddress =self.request.user.ip_address
        if ip_ddress not in article.hits.all():
            article.hits.add(ip_ddress)
    
        return article

class ArticlePreview(AuthorAccessMixin , DetailView):
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=pk )
    
    
    
# My few to many to many information.
# def category(request , slug , page=1):
#     category = get_object_or_404(Category, slug=slug , status=True)
#     article_list = category.articles.status()
#     paginator = Paginator(article_list , 3)
#     # page = request.GET.get('p')
#     article = paginator.get_page(page)
#     context =  {
#         'category':category,
#         'articles':article
#     }
#     return render(request , "prj/category.html" , context)

class categoryList(ListView):
    paginate_by = 3
    template_name = "prj/category_list.html"
    # context_object_name = "articles"
    
    def get_queryset(self) :
        global  category
        slug = self.kwargs.get('slug')
        category =  get_object_or_404(Category.objects.active() , slug=slug )
        return category.articles.status()
    
#easy codeing   
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['category'] = category
        return context
#hard codeing    
    # def get_context_data(self, **kwargs):
    #     slug = self.kwargs.get('slug')
    #     context =  super().get_context_data(**kwargs)
    #     context['category'] = get_object_or_404(Category.objects.active() , slug=slug )
    #     return context
class authorList(ListView):
    paginate_by = 3
    template_name = "prj/author_list.html"

    
    def get_queryset(self) :
        global  author
        username = self.kwargs.get('username')
        author =  get_object_or_404(User , username=username)
        return author.articles.status()
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['author'] = author
        return context