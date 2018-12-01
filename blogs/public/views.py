from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

from django.views import generic
from .models import blogs
from django.views.generic import CreateView,DeleteView,View
from django.urls import reverse,reverse_lazy
from .form import UserForm



class IndexView(generic.ListView):
    template_name='public/index.html'
    def get_queryset(self):
        return blogs.objects.all()


class PostBlogs(CreateView):
    model = blogs
    fields = ['user','heading','content']
    success_url = reverse_lazy('public:index')

class DeleteBlogs(DeleteView):
    model = blogs
    success_url = reverse_lazy('public:index')

class UserFormViewRegister(View):
    form_class = UserForm
    template_name = 'public/registeration_form.html'
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return redirect('public:index')


class UserFormViewLogin(View):
    form_class = UserForm
    template_name = 'public/registeration_form.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('public:index')
            else:
                return redirect('public:login')
        else:
            return redirect('public:login')

def logout_view(request):
    logout(request)
    return redirect('public:index')
