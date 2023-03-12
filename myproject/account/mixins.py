from django.http import Http404
from prj.models import Article
from django.shortcuts import get_object_or_404 , redirect

class FieldsMixin():
    def dispatch(self, request, *args, **kwargs):
        self.fields = [
            "name","slug",
            "is_special" , "images",
            "category","descriptions", 
            "publish", "status"
        ]
        if request.user.is_superuser:
            self.fields.append("author")
        return super().dispatch(request, *args, **kwargs)

class FormValidMixin():
    def form_valid(self , form):
        if self.request.user.is_superuser:
            form.save()        
        else:
            self.obj = form.save(commit=False)
            self.obj.author  = self.request.user   
            if not self.obj.status in ['F' , 'i']:
                self.obj.status = 'F'
        return super().form_valid(form)

class AuthorAccessMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Article , pk=pk)
        if article.author == request.user and article.status in ['F' , 'b'] or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("you can't see this page.") 
        
class AuthorsAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser or request.user.is_author:
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect("account:profile")                
        else:
            return redirect("login")
        

class SuperUserAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("you can't see this page.") 
        
